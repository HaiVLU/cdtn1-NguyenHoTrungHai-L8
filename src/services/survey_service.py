
from sqlalchemy.exc import IntegrityError

from src.extensions import db
from src.repositories import survey_repository as repo


class ValidationError(Exception):
    """Lỗi dữ liệu hoặc quy tắc nghiệp vụ."""
    pass


def serialize(survey):
    return {
        "response_id": survey.response_id,
        "ticket_id": survey.ticket_id,
        "date_id": survey.date_id,
        "score": survey.score,
        "nps_score": survey.nps_score,
        "comment": survey.comment,
        "responded_at": (
            survey.responded_at.isoformat()
            if survey.responded_at else None
        ),
    }


def validate(data):
    """Kiểm tra dữ liệu khảo sát."""

    if not isinstance(data, dict):
        raise ValidationError(
            "Dữ liệu phải là JSON object."
        )

    required = [
        "ticket_id",
        "date_id",
        "score",
        "nps_score"
    ]

    missing = [
        key for key in required
        if key not in data
    ]

    if missing:
        raise ValidationError(
            f"Thiếu trường bắt buộc: {', '.join(missing)}"
        )

    for key in required:
        if type(data[key]) is not int:
            raise ValidationError(
                f"{key} phải là số nguyên."
            )

    if data["ticket_id"] <= 0:
        raise ValidationError(
            "ticket_id phải lớn hơn 0."
        )

    if data["date_id"] <= 0:
        raise ValidationError(
            "date_id phải lớn hơn 0."
        )

    if not 1 <= data["score"] <= 5:
        raise ValidationError(
            "score phải nằm trong khoảng 1–5."
        )

    if not 0 <= data["nps_score"] <= 10:
        raise ValidationError(
            "nps_score phải nằm trong khoảng 0–10."
        )

    comment = data.get("comment")

    if comment is not None and not isinstance(comment, str):
        raise ValidationError(
            "comment phải là chuỗi hoặc null."
        )

    return data


def validate_business_rules(data, current_response_id=None):
    """
    Kiểm tra QT-10:
    - Ticket phải tồn tại.
    - Ticket phải ở trạng thái đã đóng.
    - Mỗi ticket chỉ được khảo sát một lần.
    """

    ticket = repo.get_ticket_by_id(
        data["ticket_id"]
    )

    if ticket is None:
        raise ValidationError(
            "Không tìm thấy phiếu bảo hành."
        )

    # Chuẩn hóa trạng thái ticket.
    status = (
        str(ticket.status).strip().upper()
        if ticket.status else ""
    )

    # Chấp nhận giá trị cũ trong database
    # và giá trị chuẩn đang sử dụng.
    closed_statuses = {
        "CLOSED",
        "ĐÃ ĐÓNG"
    }

    if status not in closed_statuses:
        raise ValidationError(
            "Chỉ được tạo khảo sát cho phiếu bảo hành đã đóng."
        )

    # Kiểm tra ngày khảo sát.
    date_record = repo.get_date_by_id(
        data["date_id"]
    )

    if date_record is None:
        raise ValidationError(
            "Không tìm thấy ngày khảo sát."
        )

    # Bao gồm cả bản ghi đã xóa mềm.
    existing = repo.get_by_ticket_id(
        data["ticket_id"]
    )

    if (
        existing is not None
        and existing.response_id != current_response_id
    ):
        raise ValidationError(
            "Phiếu bảo hành này đã có khảo sát."
        )


def list_surveys():
    surveys = repo.get_all()

    return [
        serialize(survey)
        for survey in surveys
    ]


def get_survey(response_id):
    survey = repo.get_by_id(response_id)

    if survey is None:
        return None

    return serialize(survey)


def create_survey(data):
    validate(data)

    validate_business_rules(data)

    try:
        survey = repo.create(data)

        return serialize(survey)

    except IntegrityError:
        db.session.rollback()

        raise ValidationError(
            "Dữ liệu liên kết không hợp lệ "
            "hoặc phiếu bảo hành đã có khảo sát."
        )


def update_survey(response_id, data):
    validate(data)

    survey = repo.get_by_id(response_id)

    if survey is None:
        return None

    validate_business_rules(
        data,
        current_response_id=survey.response_id
    )

    try:
        updated = repo.update(survey, data)

        return serialize(updated)

    except IntegrityError:
        db.session.rollback()

        raise ValidationError(
            "Dữ liệu liên kết không hợp lệ "
            "hoặc phiếu bảo hành đã có khảo sát."
        )


def delete_survey(response_id):
    survey = repo.get_by_id(response_id)

    if survey is None:
        return False

    try:
        repo.soft_delete(survey)

        return True

    except IntegrityError:
        db.session.rollback()
        raise
