# API Contract – L8 CSAT/NPS

## 1. GET /api/csat-nps/time

### Mục đích

Lấy kết quả CSAT/NPS theo khoảng thời gian.

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Response 200

```json
{
  "from_date": "2026-01-01",
  "to_date": "2026-01-31",
  "csat_score": 85.5,
  "nps_score": 42
}
```

### Errors

- 400: Khoảng thời gian không hợp lệ.
- 403: Người dùng không có quyền truy cập.
- 404: Không có dữ liệu khảo sát.

---

## 2. GET /api/csat-nps/centers

### Mục đích

Lấy kết quả CSAT/NPS theo trung tâm.

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | integer | Yes | Mã trung tâm |
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Response 200

```json
{
  "center_id": 101,
  "center_name": "Trung tâm A",
  "csat_score": 86.2,
  "nps_score": 45
}
```

### Errors

- 400: Tham số không hợp lệ.
- 403: Không có quyền truy cập dữ liệu.
- 404: Không có dữ liệu khảo sát.

---

## 3. GET /api/csat-nps/technicians

### Mục đích

Lấy kết quả CSAT/NPS theo từng kỹ thuật viên thuộc trung tâm được phân quyền.

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | integer | Yes | Mã trung tâm |
| technician_id | integer | No | Mã kỹ thuật viên |
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Response 200

```json
{
  "center_id": 101,
  "technicians": [
    {
      "technician_id": 1001,
      "technician_name": "Technician A",
      "csat_score": 88.5,
      "nps_score": 50
    }
  ]
}
```

### Errors

- 400: Khoảng thời gian không hợp lệ.
- 403: Người dùng cố truy cập dữ liệu ngoài phạm vi được phân quyền.
- 404: Không có dữ liệu khảo sát.
