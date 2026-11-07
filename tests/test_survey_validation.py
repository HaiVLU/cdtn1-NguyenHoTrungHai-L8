from types import SimpleNamespace

import pytest

from src.services import survey_service
from src.services.survey_service import ValidationError, validate


def valid_data(**overrides):
    data = {
        "ticket_id": 1001,
        "date_id": 20261001,
        "score": 5,
        "nps_score": 10,
        "comment": "Dịch vụ tốt, nhân viên nhiệt tình.",
    }
    data.update(overrides)
    return data


# 1. POSITIVE – dữ liệu hợp lệ và các trường không bắt buộc
def test_positive_valid_survey_data():
    data = valid_data()
    assert validate(data) == data


def test_positive_comment_is_optional():
    data = valid_data()
    data.pop("comment")
    assert validate(data) == data


def test_positive_comment_can_be_null():
    data = valid_data(comment=None)
    assert validate(data) == data


# 2. BOUNDARY – kiểm tra các giá trị biên hợp lệ
@pytest.mark.parametrize(
    "field,value",
    [
        ("score", 1),
        ("score", 5),
        ("nps_score", 0),
        ("nps_score", 10),
    ],
)
def test_boundary_valid_minimum_and_maximum(field, value):
    data = valid_data(**{field: value})
    assert validate(data)[field] == value


# 3. NEGATIVE – kiểm tra cấu trúc và dữ liệu không hợp lệ
@pytest.mark.parametrize("data", [None, [], "survey", 123])
def test_negative_body_must_be_json_object(data):
    with pytest.raises(ValidationError, match="JSON object"):
        validate(data)


@pytest.mark.parametrize(
    "missing_field",
    ["ticket_id", "date_id", "score", "nps_score"],
)
def test_negative_missing_required_field(missing_field):
    data = valid_data()
    data.pop(missing_field)
    with pytest.raises(ValidationError, match=missing_field):
        validate(data)


@pytest.mark.parametrize(
    "field,value",
    [
        ("ticket_id", "1001"),
        ("date_id", "20261001"),
        ("score", "5"),
        ("nps_score", "10"),
        ("score", True),
    ],
)
def test_negative_invalid_integer_type(field, value):
    with pytest.raises(ValidationError, match=field):
        validate(valid_data(**{field: value}))


@pytest.mark.parametrize("field,value", [("ticket_id", 0), ("ticket_id", -1)])
def test_negative_ticket_id_must_be_positive(field, value):
    with pytest.raises(ValidationError, match="ticket_id"):
        validate(valid_data(**{field: value}))


def test_negative_date_id_must_be_positive():
    with pytest.raises(ValidationError, match="date_id"):
        validate(valid_data(date_id=0))


@pytest.mark.parametrize("score", [0, 6, -1])
def test_negative_csat_out_of_range(score):
    with pytest.raises(ValidationError, match="score"):
        validate(valid_data(score=score))


@pytest.mark.parametrize("nps_score", [-1, 11])
def test_negative_nps_out_of_range(nps_score):
    with pytest.raises(ValidationError, match="nps_score"):
        validate(valid_data(nps_score=nps_score))


def test_negative_comment_must_be_string_or_null():
    with pytest.raises(ValidationError, match="comment"):
        validate(valid_data(comment=123))


# 4. BUSINESS RULE / DATA QUALITY – mock repository, không ghi vào DB thật
def configure_business_rule_mocks(
    monkeypatch,
    *,
    ticket_status="CLOSED",
    ticket_exists=True,
    date_exists=True,
    existing_survey=None,
):
    repo = survey_service.repo
    monkeypatch.setattr(
        repo,
        "get_ticket_by_id",
        lambda ticket_id: (
            SimpleNamespace(status=ticket_status)
            if ticket_exists else None
        ),
    )
    monkeypatch.setattr(
        repo,
        "get_date_by_id",
        lambda date_id: (
            SimpleNamespace(date_id=date_id)
            if date_exists else None
        ),
    )
    monkeypatch.setattr(
        repo,
        "get_by_ticket_id",
        lambda ticket_id: existing_survey,
    )


def test_business_ticket_must_exist(monkeypatch):
    configure_business_rule_mocks(monkeypatch, ticket_exists=False)
    with pytest.raises(ValidationError, match="phiếu bảo hành"):
        survey_service.validate_business_rules(valid_data())


@pytest.mark.parametrize("status", ["OPEN", "PENDING", "IN_PROGRESS"])
def test_business_ticket_must_be_closed(monkeypatch, status):
    configure_business_rule_mocks(monkeypatch, ticket_status=status)
    with pytest.raises(ValidationError, match="đã đóng"):
        survey_service.validate_business_rules(valid_data())


def test_business_accepts_closed_status_with_vietnamese_value(monkeypatch):
    configure_business_rule_mocks(monkeypatch, ticket_status=" Đã đóng ")
    survey_service.validate_business_rules(valid_data())


def test_business_survey_date_must_exist(monkeypatch):
    configure_business_rule_mocks(monkeypatch, date_exists=False)
    with pytest.raises(ValidationError, match="ngày khảo sát"):
        survey_service.validate_business_rules(valid_data())


def test_data_quality_ticket_cannot_have_duplicate_survey(monkeypatch):
    existing = SimpleNamespace(response_id=77)
    configure_business_rule_mocks(monkeypatch, existing_survey=existing)
    with pytest.raises(ValidationError, match="đã có khảo sát"):
        survey_service.validate_business_rules(valid_data())


def test_business_same_record_can_be_validated_during_update(monkeypatch):
    existing = SimpleNamespace(response_id=77)
    configure_business_rule_mocks(monkeypatch, existing_survey=existing)
    survey_service.validate_business_rules(
        valid_data(),
        current_response_id=77,
    )


def test_reproducibility_validation_returns_same_result():
    data = valid_data()
    first_result = validate(data)
    second_result = validate(data.copy())
    assert first_result == second_result
