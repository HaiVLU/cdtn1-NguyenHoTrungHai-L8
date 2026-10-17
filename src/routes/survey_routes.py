from flask import Blueprint, request
from src.services import survey_service as service

survey_bp = Blueprint("surveys", __name__)


@survey_bp.get("")
def list_surveys():
    return {"data": service.list_surveys()}, 200


@survey_bp.get("/<int:response_id>")
def get_survey(response_id):
    survey = service.get_survey(response_id)

    if survey is None:
        return {"error": "Không tìm thấy khảo sát."}, 404

    return {"data": survey}, 200


@survey_bp.post("")
def create_survey():
    data = request.get_json(silent=True)

    if data is None:
        return {"error": "Request body phải là JSON hợp lệ."}, 400

    try:
        survey = service.create_survey(data)
        return {"message": "Tạo khảo sát thành công.", "data": survey}, 201
    except service.ValidationError as exc:
        return {"error": str(exc)}, 400


@survey_bp.put("/<int:response_id>")
def update_survey(response_id):
    data = request.get_json(silent=True)

    if data is None:
        return {"error": "Request body phải là JSON hợp lệ."}, 400

    try:
        survey = service.update_survey(response_id, data)

        if survey is None:
            return {"error": "Không tìm thấy khảo sát."}, 404

        return {"message": "Cập nhật thành công.", "data": survey}, 200
    except service.ValidationError as exc:
        return {"error": str(exc)}, 400


@survey_bp.delete("/<int:response_id>")
def delete_survey(response_id):
    if not service.delete_survey(response_id):
        return {"error": "Không tìm thấy khảo sát."}, 404

    return {"message": "Xóa khảo sát thành công."}, 200