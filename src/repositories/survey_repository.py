from src.extensions import db
from src.models import SurveyResponse


def get_all():
    return SurveyResponse.query.order_by(
        SurveyResponse.response_id
    ).all()


def get_by_id(response_id):
    return db.session.get(SurveyResponse, response_id)


def create(data):
    survey = SurveyResponse(
        ticket_id=data["ticket_id"],
        date_id=data["date_id"],
        score=data["score"],
        nps_score=data["nps_score"],
        comment=data.get("comment"),
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


def delete(survey):
    db.session.delete(survey)
    db.session.commit()