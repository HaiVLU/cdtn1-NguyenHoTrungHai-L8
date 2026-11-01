
import pytest

from src.services.survey_service import (
    validate,
    ValidationError
)


# ==========================================
# TEST 1: POSITIVE
# Dữ liệu hợp lệ thông thường
# ==========================================

def test_positive_valid_survey_data():
    data = {
        "ticket_id": 1001,
        "date_id": 20261001,
        "score": 5,
        "nps_score": 10,
        "comment": "Dịch vụ tốt, nhân viên nhiệt tình."
    }

    result = validate(data)

    assert result == data


# ==========================================
# TEST 2: BOUNDARY
# Kiểm tra giá trị biên hợp lệ
# ==========================================

def test_boundary_minimum_valid_scores():
    data = {
        "ticket_id": 1002,
        "date_id": 20261001,
        "score": 1,
        "nps_score": 0,
        "comment": "Điểm đánh giá ở giới hạn dưới."
    }

    result = validate(data)

    assert result == data


# ==========================================
# TEST 3: NEGATIVE
# Thiếu trường bắt buộc
# ==========================================

def test_negative_missing_required_field():
    data = {
        "date_id": 20261001,
        "score": 5,
        "nps_score": 10
    }

    with pytest.raises(
        ValidationError,
        match="ticket_id"
    ):
        validate(data)


# ==========================================
# TEST 4: NEGATIVE
# Điểm CSAT vượt giới hạn
# ==========================================

def test_negative_invalid_csat_score():
    data = {
        "ticket_id": 1003,
        "date_id": 20261001,
        "score": 6,
        "nps_score": 10
    }

    with pytest.raises(
        ValidationError,
        match="score"
    ):
        validate(data)


# ==========================================
# TEST 5: NEGATIVE
# Sai kiểu dữ liệu
# ==========================================

def test_negative_invalid_data_type():
    data = {
        "ticket_id": 1004,
        "date_id": 20261001,
        "score": "5",
        "nps_score": 10
    }

    with pytest.raises(
        ValidationError,
        match="score"
    ):
        validate(data)
