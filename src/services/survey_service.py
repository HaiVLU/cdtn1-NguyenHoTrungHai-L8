from sqlalchemy.exc import IntegrityError

from src.repositories import survey_repository as repo


class ValidationError(Exception):
    pass


def serialize(survey):
    return {
        "response_id": survey.response_id,
        "ticket_id": survey.ticket_id,
        "date_id": survey.date_id,
        "score": survey.score,
        "nps_score": survey.nps_score,
        "comment": survey.comment,
        "responded_at": survey.responded_at.isoformat(),
    }


def validate(data):
    required = ["ticket_id", "date_id", "score", "nps_score"]

    if not isinstance(data, dict):
        raise ValidationError("Dữ liệu phải là JSON object.")

    missing = [key for key in required if key not in data]
    if missing:
        raise ValidationError(
            f"Thiếu trường bắt buộc: {', '.join(missing)}"
        )

    for key in ["ticket_id", "date_id", "score", "nps_score"]:
        if type(data[key]) is not int:
            raise ValidationError(f"{key} phải là số nguyên.")

    if data["ticket_id"] <= 0 or data["date_id"] <= 0:
        raise ValidationError("ticket_id và date_id phải lớn hơn 0.")

    if not 1 <= data["score"] <= 5:
        raise ValidationError("score phải nằm trong khoảng 1–5.")

    if not 0 <= data["nps_score"] <= 10:
        raise ValidationError("nps_score phải nằm trong khoảng 0–10.")

    if "comment" in data and data["comment"] is not None:
        if not isinstance(data["comment"], str):
            raise ValidationError("comment phải là chuỗi hoặc null.")

    return data


def list_surveys():
    return [serialize(s) for s in repo.get_all()]


def get_survey(response_id):
    survey = repo.get_by_id(response_id)
    if survey is None:
        return None
    return serialize(survey)


def create_survey(data):
    validate(data)
    try:
        survey = repo.create(data)
        return serialize(survey)
    except IntegrityError:
        from src.extensions import db
        db.session.rollback()
        raise ValidationError(
            "ticket_id hoặc date_id không hợp lệ, "
            "hoặc phiếu đã có khảo sát."
        )


def update_survey(response_id, data):
    validate(data)
    survey = repo.get_by_id(response_id)

    if survey is None:
        return None

    try:
        return serialize(repo.update(survey, data))
    except IntegrityError:
        from src.extensions import db
        db.session.rollback()
        raise ValidationError(
            "Dữ liệu liên kết không hợp lệ hoặc phiếu đã có khảo sát."
        )


def delete_survey(response_id):
    survey = repo.get_by_id(response_id)
    if survey is None:
        return False

    repo.delete(survey)
    return True