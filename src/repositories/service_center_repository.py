
from src.extensions import db
from src.models import ServiceCenter, Technician, Ticket


def get_all():
    return ServiceCenter.query.order_by(
        ServiceCenter.center_id
    ).all()


def get_by_id(center_id):
    return db.session.get(
        ServiceCenter,
        center_id
    )


def has_dependencies(center_id):
    """
    Kiểm tra trung tâm có đang được
    kỹ thuật viên hoặc phiếu bảo hành sử dụng không.
    """

    has_technician = Technician.query.filter_by(
        center_id=center_id
    ).first() is not None

    has_ticket = Ticket.query.filter_by(
        center_id=center_id
    ).first() is not None

    return has_technician or has_ticket


def create(data):
    center = ServiceCenter(
        center_name=data["center_name"]
    )

    db.session.add(center)
    db.session.commit()

    return center


def update(center, data):
    center.center_name = data["center_name"]

    db.session.commit()

    return center


def delete(center):
    db.session.delete(center)
    db.session.commit()
