from datetime import date, datetime

from src import create_app
from src.extensions import db
from src.models import (
    Customer,
    ServiceCenter,
    Technician,
    DimDate,
    Ticket,
    SurveyResponse,
)

app = create_app()

with app.app_context():
    # Tránh thêm dữ liệu trùng nếu chạy seed nhiều lần
    if db.session.query(ServiceCenter).first():
        print("Đã có dữ liệu mẫu. Không nạp trùng.")
    else:
        center1 = ServiceCenter(center_name="Trung tâm Quận 10")
        center2 = ServiceCenter(center_name="Trung tâm Cần Thơ")
        db.session.add_all([center1, center2])
        db.session.flush()

        tech1 = Technician(
            center_id=center1.center_id,
            technician_name="Nguyễn Văn An",
        )
        tech2 = Technician(
            center_id=center2.center_id,
            technician_name="Trần Văn Bình",
        )

        customer1 = Customer(
            full_name="Khách hàng mẫu 01",
            phone="0900000001",
        )
        customer2 = Customer(
            full_name="Khách hàng mẫu 02",
            phone="0900000002",
        )

        db.session.add_all([tech1, tech2, customer1, customer2])
        db.session.flush()

        today = date.today()
        quarter = (today.month - 1) // 3 + 1

        date_record = DimDate(
            full_date=today,
            month=today.month,
            quarter=quarter,
            year=today.year,
        )
        db.session.add(date_record)
        db.session.flush()

        ticket1 = Ticket(
            customer_id=customer1.customer_id,
            center_id=center1.center_id,
            technician_id=tech1.technician_id,
            status="ĐÃ ĐÓNG",
            closed_at=datetime.now(),
        )
        ticket2 = Ticket(
            customer_id=customer2.customer_id,
            center_id=center2.center_id,
            technician_id=tech2.technician_id,
            status="ĐÃ ĐÓNG",
            closed_at=datetime.now(),
        )

        db.session.add_all([ticket1, ticket2])
        db.session.flush()

        survey1 = SurveyResponse(
            ticket_id=ticket1.ticket_id,
            date_id=date_record.date_id,
            score=5,
            nps_score=9,
            comment="Dịch vụ tốt.",
            responded_at=datetime.now(),
        )
        survey2 = SurveyResponse(
            ticket_id=ticket2.ticket_id,
            date_id=date_record.date_id,
            score=4,
            nps_score=8,
            comment="Nhân viên hỗ trợ nhiệt tình.",
            responded_at=datetime.now(),
        )

        db.session.add_all([survey1, survey2])
        db.session.commit()

        print("Đã nạp dữ liệu mẫu thành công.")