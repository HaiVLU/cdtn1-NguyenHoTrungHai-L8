
from sqlalchemy.exc import IntegrityError

from src.extensions import db
from src.repositories import service_center_repository as repo


class ValidationError(Exception):
    pass


class ConflictError(Exception):
    pass


def validate(data):
    if not isinstance(data, dict):
        raise ValidationError(
            "Dữ liệu phải là JSON object."
        )

    if "center_name" not in data:
        raise ValidationError(
            "Thiếu trường bắt buộc: center_name."
        )

    center_name = data["center_name"]

    if not isinstance(center_name, str):
        raise ValidationError(
            "center_name phải là chuỗi."
        )

    center_name = center_name.strip()

    if not center_name:
        raise ValidationError(
            "Tên trung tâm không được để trống."
        )

    if len(center_name) > 100:
        raise ValidationError(
            "Tên trung tâm không được vượt quá 100 ký tự."
        )

    return {
        "center_name": center_name
    }


def serialize(center):
    return {
        "center_id": center.center_id,
        "center_name": center.center_name
    }


def list_centers():
    centers = repo.get_all()

    return [
        serialize(center)
        for center in centers
    ]


def get_center(center_id):
    center = repo.get_by_id(center_id)

    if center is None:
        return None

    return serialize(center)


def create_center(data):
    validated_data = validate(data)

    try:
        center = repo.create(validated_data)

        return serialize(center)

    except IntegrityError:
        db.session.rollback()

        raise ConflictError(
            "Không thể tạo trung tâm với dữ liệu hiện tại."
        )


def update_center(center_id, data):
    validated_data = validate(data)

    center = repo.get_by_id(center_id)

    if center is None:
        return None

    try:
        center = repo.update(
            center,
            validated_data
        )

        return serialize(center)

    except IntegrityError:
        db.session.rollback()

        raise ConflictError(
            "Không thể cập nhật trung tâm."
        )


def delete_center(center_id):
    center = repo.get_by_id(center_id)

    if center is None:
        return False

    if repo.has_dependencies(center_id):
        raise ConflictError(
            "Không thể xóa trung tâm vì đang có "
            "kỹ thuật viên hoặc phiếu bảo hành liên kết."
        )

    try:
        repo.delete(center)

        return True

    except IntegrityError:
        db.session.rollback()

        raise ConflictError(
            "Không thể xóa trung tâm do đang có dữ liệu liên kết."
        )
