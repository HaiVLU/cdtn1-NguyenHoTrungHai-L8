
from datetime import date
import logging

from flask import Blueprint, request
from sqlalchemy import func

from src.extensions import db
from src.models import (
    DimDate,
    ServiceCenter,
    SurveyResponse,
    Technician,
    Ticket,
)

report_bp = Blueprint("csat_nps_reports", __name__)

logger = logging.getLogger(__name__)


def parse_date(value, field_name):
    """Parse date in YYYY-MM-DD format."""
    if not value:
        return None

    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        raise ValueError(
            f"{field_name} must use YYYY-MM-DD format."
        )


def get_records():
    """Get survey responses associated with closed tickets."""

    query = (
        db.session.query(
            SurveyResponse.response_id,
            SurveyResponse.score,
            SurveyResponse.nps_score,
            DimDate.full_date,
            Ticket.center_id,
            ServiceCenter.center_name,
            Ticket.technician_id,
            Technician.technician_name,
        )
        .join(
            DimDate,
            SurveyResponse.date_id == DimDate.date_id,
        )
        .join(
            Ticket,
            SurveyResponse.ticket_id == Ticket.ticket_id,
        )
        .join(
            ServiceCenter,
            Ticket.center_id == ServiceCenter.center_id,
        )
        .outerjoin(
            Technician,
            Ticket.technician_id == Technician.technician_id,
        )
    )

    # Chỉ lấy khảo sát chưa bị xóa mềm.
    query = query.filter(
        SurveyResponse.is_deleted.is_(False)
    )

    # Chấp nhận trạng thái chuẩn và dữ liệu cũ.
    query = query.filter(
        func.upper(func.trim(Ticket.status)).in_(
            ["CLOSED", "ĐÃ ĐÓNG"]
        )
    )

    # Lọc ngày bắt đầu và ngày kết thúc.
    start_date = parse_date(
        request.args.get("startDate"), "startDate"
    )

    end_date = parse_date(
        request.args.get("endDate"), "endDate"
    )

    if start_date and end_date and start_date > end_date:
        raise ValueError(
            "startDate must not be after endDate."
        )

    if start_date:
        query = query.filter(
            DimDate.full_date >= start_date
        )

    if end_date:
        query = query.filter(
            DimDate.full_date <= end_date
        )

    # Lọc trung tâm dịch vụ.
    center_id = request.args.get("centerId")

    if center_id:
        try:
            center_id = int(center_id)

            if center_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            raise ValueError(
                "centerId must be a positive integer."
            )

        query = query.filter(
            Ticket.center_id == center_id
        )

    return query.order_by(DimDate.full_date).all()


def calculate_metrics(records):
    """
    Calculate average CSAT and average survey rating on a 1–10 scale.
    """

    count = len(records)

    if count == 0:
        return {
            "surveyCount": 0,
            "csat": {
                "averageScore": None,
            },
            "nps": {
                "score": None,
                "status": "unavailable",
            },
        }

    valid_scores = [
        row.score
        for row in records
        if row.score is not None
    ]

    valid_nps = [
        row.nps_score
        for row in records
        if row.nps_score is not None
    ]

    average_score = (
        round(
            sum(valid_scores) / len(valid_scores),
            2
        )
        if valid_scores
        else None
    )

    # Hiển thị điểm NPS trung bình trên thang 1–10.
    nps_score = (
        round(
            sum(valid_nps) / len(valid_nps),
            2
        )
        if valid_nps
        else None
    )

    return {
        "surveyCount": count,
        "csat": {
            "averageScore": average_score,
        },
        "nps": {
            "score": nps_score,
            "status": (
                "available" if valid_nps else "unavailable"
            ),
        },
    }


def error_response(message, status_code=400):
    return {"message": message}, status_code


def handle_report_error(exc):
    """Log errors without requiring a Windows terminal to encode Unicode."""

    logger.error(
        "Report API failed: %s",
        str(exc).encode(
            "ascii",
            errors="backslashreplace",
        ).decode("ascii"),
        exc_info=True,
    )

    return error_response(
        "Report processing failed. Check the Flask terminal log.",
        500,
    )


@report_bp.get("/summary")
def summary():
    try:
        records = get_records()

        return {
            "data": calculate_metrics(records)
        }, 200

    except ValueError as exc:
        return error_response(str(exc), 400)

    except Exception as exc:
        return handle_report_error(exc)


@report_bp.get("/trend")
def trend():
    try:
        records = get_records()

        group_by = request.args.get(
            "groupBy", "day"
        ).lower()

        if group_by not in ("day", "month"):
            return error_response(
                "groupBy must be day or month.",
                400,
            )

        groups = {}

        for row in records:
            if row.full_date is None:
                continue

            period = (
                row.full_date.isoformat()
                if group_by == "day"
                else row.full_date.strftime("%Y-%m")
            )

            groups.setdefault(period, []).append(row)

        items = []

        for period, group_records in sorted(groups.items()):

            metrics = calculate_metrics(group_records)

            items.append({
                "period": period,
                "surveyCount": metrics["surveyCount"],
                "csat": metrics["csat"],
                "nps": metrics["nps"],
            })

        return {
            "data": {
                "items": items
            }
        }, 200

    except ValueError as exc:
        return error_response(str(exc), 400)

    except Exception as exc:
        return handle_report_error(exc)


@report_bp.get("/centers")
def centers():
    try:
        records = get_records()

        grouped = {}

        for row in records:

            item = grouped.setdefault(
                row.center_id,
                {
                    "centerId": row.center_id,
                    "centerName": row.center_name,
                    "records": [],
                },
            )

            item["records"].append(row)

        items = []

        for item in grouped.values():

            metrics = calculate_metrics(
                item.pop("records")
            )

            items.append({
                **item,
                **metrics
            })

        # Bao gồm cả trung tâm chưa có khảo sát
        # trong khoảng thời gian được chọn.
        existing_ids = {
            item["centerId"] for item in items
        }

        all_centers = ServiceCenter.query.order_by(
            ServiceCenter.center_id
        ).all()

        for center in all_centers:

            if center.center_id not in existing_ids:

                items.append({
                    "centerId": center.center_id,
                    "centerName": center.center_name,
                    **calculate_metrics([]),
                })

        return {
            "data": {
                "items": sorted(
                    items,
                    key=lambda item: item["centerId"],
                )
            }
        }, 200

    except ValueError as exc:
        return error_response(str(exc), 400)

    except Exception as exc:
        return handle_report_error(exc)


@report_bp.get("/technicians")
def technicians():
    try:
        records = get_records()

        grouped = {}

        for row in records:

            if row.technician_id is None:
                continue

            item = grouped.setdefault(
                row.technician_id,
                {
                    "technicianId": row.technician_id,
                    "technicianName": row.technician_name,
                    "centerId": row.center_id,
                    "centerName": row.center_name,
                    "records": [],
                },
            )

            item["records"].append(row)

        items = []

        for item in grouped.values():

            metrics = calculate_metrics(
                item.pop("records")
            )

            items.append({
                **item,
                **metrics
            })

        return {
            "data": {
                "items": sorted(
                    items,
                    key=lambda item: item["technicianId"],
                )
            }
        }, 200

    except ValueError as exc:
        return error_response(str(exc), 400)

    except Exception as exc:
        return handle_report_error(exc)


@report_bp.get("/centers/<int:center_id>")
def center_detail(center_id):
    try:
        center = db.session.get(
            ServiceCenter,
            center_id,
        )

        if center is None:
            return error_response(
                "Center not found.",
                404,
            )

        records = get_records()

        center_records = [
            row
            for row in records
            if row.center_id == center_id
        ]

        return {
            "data": {
                "centerId": center.center_id,
                "centerName": center.center_name,
                **calculate_metrics(center_records),
            }
        }, 200

    except ValueError as exc:
        return error_response(str(exc), 400)

    except Exception as exc:
        return handle_report_error(exc)
