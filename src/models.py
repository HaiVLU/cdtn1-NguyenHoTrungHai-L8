from datetime import datetime
from .extensions import db


class Customer(db.Model):
    __tablename__ = "customer"

    customer_id = db.Column(db.BigInteger, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)


class ServiceCenter(db.Model):
    __tablename__ = "service_center"

    center_id = db.Column(db.BigInteger, primary_key=True)
    center_name = db.Column(db.String(100), nullable=False)


class Technician(db.Model):
    __tablename__ = "technician"

    technician_id = db.Column(db.BigInteger, primary_key=True)
    center_id = db.Column(
        db.BigInteger,
        db.ForeignKey("service_center.center_id"),
        nullable=False,
    )
    technician_name = db.Column(db.String(100), nullable=False)


class DimDate(db.Model):
    __tablename__ = "dim_date"

    date_id = db.Column(db.BigInteger, primary_key=True)
    full_date = db.Column(db.Date, nullable=False, unique=True)
    month = db.Column(db.SmallInteger, nullable=False)
    quarter = db.Column(db.SmallInteger, nullable=False)
    year = db.Column(db.SmallInteger, nullable=False)


class Ticket(db.Model):
    __tablename__ = "ticket"

    ticket_id = db.Column(db.BigInteger, primary_key=True)
    customer_id = db.Column(
        db.BigInteger, db.ForeignKey("customer.customer_id"),
        nullable=False,
    )
    center_id = db.Column(
        db.BigInteger, db.ForeignKey("service_center.center_id"),
        nullable=False,
    )
    technician_id = db.Column(
        db.BigInteger, db.ForeignKey("technician.technician_id"),
        nullable=True,
    )
    status = db.Column(db.String(20), nullable=False)
    closed_at = db.Column(db.DateTime, nullable=True)


class SurveyResponse(db.Model):
    __tablename__ = "survey_response"

    response_id = db.Column(db.BigInteger, primary_key=True)
    ticket_id = db.Column(
        db.BigInteger,
        db.ForeignKey("ticket.ticket_id"),
        nullable=False,
        unique=True,
    )
    date_id = db.Column(
        db.BigInteger,
        db.ForeignKey("dim_date.date_id"),
        nullable=False,
    )
    score = db.Column(db.SmallInteger, nullable=False)
    nps_score = db.Column(db.SmallInteger, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    responded_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now,
    )

    __table_args__ = (
        db.CheckConstraint(
            "score BETWEEN 1 AND 5",
            name="ck_survey_score",
        ),
        db.CheckConstraint(
            "nps_score BETWEEN 0 AND 10",
            name="ck_survey_nps_score",
        ),
    )