
from src.extensions import db
from src.models import SurveyResponse, Ticket, DimDate


def get_all():
    """Lấy danh sách khảo sát chưa bị xóa mềm."""
    return SurveyResponse.query.filter(
        SurveyResponse.is_deleted.is_(False)
    ).order_by(
        SurveyResponse.response_id
    ).all()


def get_by_id(response_id):
    """Lấy khảo sát theo ID, không lấy bản ghi đã xóa."""
    return SurveyResponse.query.filter_by(
        response_id=response_id,
        is_deleted=False
    ).first()


def get_by_ticket_id(ticket_id):
    """
    Tìm khảo sát theo ticket.
    Bao gồm cả khảo sát đã xóa mềm để bảo vệ QT-10.
    """
    return SurveyResponse.query.filter_by(
        ticket_id=ticket_id
    ).first()


def get_ticket_by_id(ticket_id):
    """Lấy thông tin phiếu bảo hành."""
    return db.session.get(Ticket, ticket_id)


def get_date_by_id(date_id):
    """Kiểm tra ngày khảo sát có tồn tại."""
    return db.session.get(DimDate, date_id)


def create(data):
    survey = SurveyResponse(
        ticket_id=data["ticket_id"],
        date_id=data["date_id"],
        score=data["score"],
        nps_score=data["nps_score"],
        comment=data.get("comment"),
        is_deleted=False
    )

    db.session.add(survey)
    db.session.commit()

    return survey


def update(survey, data):
    survey.ticket_id = data["ticket_id"]
    survey.date_id = data["date_id"]
    survey.score = data["score"]
    survey.nps_score = data["nps_score"]
    survey.comment = data.get("comment")

    db.session.commit()

    return survey


def soft_delete(survey):
    """Xóa mềm, giữ nguyên dữ liệu trong database."""
    survey.is_deleted = True

    db.session.commit()

    return survey
