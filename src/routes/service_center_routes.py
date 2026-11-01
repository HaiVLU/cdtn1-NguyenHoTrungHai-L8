
from flask import Blueprint, request

from src.services import service_center_service as service


service_center_bp = Blueprint(
    "service_centers",
    __name__
)


@service_center_bp.get("")
def list_centers():
    return {
        "data": service.list_centers()
    }, 200


@service_center_bp.get("/<int:center_id>")
def get_center(center_id):
    center = service.get_center(center_id)

    if center is None:
        return {
            "error": "Không tìm thấy trung tâm."
        }, 404

    return {
        "data": center
    }, 200


@service_center_bp.post("")
def create_center():
    data = request.get_json(silent=True)

    try:
        center = service.create_center(data)

        return {
            "message": "Tạo trung tâm thành công.",
            "data": center
        }, 201

    except service.ValidationError as exc:
        return {
            "error": str(exc)
        }, 400

    except service.ConflictError as exc:
        return {
            "error": str(exc)
        }, 409


@service_center_bp.put("/<int:center_id>")
def update_center(center_id):
    data = request.get_json(silent=True)

    try:
        center = service.update_center(
            center_id,
            data
        )

        if center is None:
            return {
                "error": "Không tìm thấy trung tâm."
            }, 404

        return {
            "message": "Cập nhật trung tâm thành công.",
            "data": center
        }, 200

    except service.ValidationError as exc:
        return {
            "error": str(exc)
        }, 400

    except service.ConflictError as exc:
        return {
            "error": str(exc)
        }, 409


@service_center_bp.delete("/<int:center_id>")
def delete_center(center_id):
    try:
        deleted = service.delete_center(center_id)

        if not deleted:
            return {
                "error": "Không tìm thấy trung tâm."
            }, 404

        return {
            "message": "Xóa trung tâm thành công."
        }, 200

    except service.ConflictError as exc:
        return {
            "error": str(exc)
        }, 409
