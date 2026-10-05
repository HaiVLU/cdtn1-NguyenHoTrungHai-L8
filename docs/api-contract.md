# API Contract – L8 CSAT/NPS

## 1. Phạm vi

API phục vụ các User Story MUST của luồng L8 – Khảo sát hài lòng CSAT/NPS.

Các User Story được hỗ trợ:

- US1 – Xem CSAT/NPS theo thời gian
- US2 – Xem CSAT/NPS theo trung tâm
- US3 – Quản lý xem CSAT/NPS của trung tâm
- US4 – Xem CSAT/NPS theo kỹ thuật viên
- US5 – Xem báo cáo tổng hợp
- US7 – Kiểm soát phạm vi dữ liệu
- US8 – Che số điện thoại khách hàng

US6 là SHOULD nên không thuộc phạm vi endpoint MUST của tài liệu này.

---

# 2. Endpoint 1 – Xem CSAT/NPS theo thời gian

## GET /api/csat-nps/time

### User Story

US1 – Xem CSAT/NPS theo thời gian.

### Mục đích

Lấy chỉ số CSAT/NPS theo khoảng thời gian để Marketing
theo dõi xu hướng hài lòng của khách hàng.

### Request

#### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Request mẫu

```json
{
  "from_date": "2026-01-01",
  "to_date": "2026-01-31"
}
```

### Response 200

```json
{
  "from_date": "2026-01-01",
  "to_date": "2026-01-31",
  "csat_score": 85.5,
  "nps_score": 42
}
```

### HTTP Status

| Status | Meaning |
|---|---|
| 200 | Lấy dữ liệu thành công |
| 400 | Dữ liệu đầu vào không hợp lệ |
| 404 | Không tìm thấy dữ liệu khảo sát |
| 409 | Xung đột dữ liệu hoặc yêu cầu không thể xử lý |

---

# 3. Endpoint 2 – Xem CSAT/NPS theo trung tâm

## GET /api/csat-nps/centers

### User Story

US2 – Xem CSAT/NPS theo trung tâm.

US3 – Quản lý xem CSAT/NPS của trung tâm.

US7 – Kiểm soát phạm vi dữ liệu.

### Mục đích

Lấy kết quả CSAT/NPS theo trung tâm.

Marketing có thể so sánh các trung tâm.

Quản lý trung tâm chỉ được xem dữ liệu của trung tâm
mình được phân quyền.

### Request

#### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | integer | No | Mã trung tâm |
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Request mẫu

```json
{
  "center_id": 101,
  "from_date": "2026-01-01",
  "to_date": "2026-01-31"
}
```

### Response 200

```json
{
  "center_id": 101,
  "center_name": "Trung tâm 101",
  "from_date": "2026-01-01",
  "to_date": "2026-01-31",
  "csat_score": 86.2,
  "nps_score": 45
}
```

### HTTP Status

| Status | Meaning |
|---|---|
| 200 | Lấy dữ liệu thành công |
| 400 | Tham số không hợp lệ |
| 404 | Không tìm thấy trung tâm hoặc dữ liệu khảo sát |
| 409 | Xung đột dữ liệu |
 
---

# 4. Endpoint 3 – Xem CSAT/NPS theo kỹ thuật viên

## GET /api/csat-nps/technicians

### User Story

US4 – Xem CSAT/NPS theo kỹ thuật viên.

US7 – Kiểm soát phạm vi dữ liệu.

### Mục đích

Lấy kết quả CSAT/NPS theo từng kỹ thuật viên thuộc
trung tâm được phân quyền.

### Request

#### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | integer | Yes | Mã trung tâm |
| technician_id | integer | No | Mã kỹ thuật viên |
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Request mẫu

```json
{
  "center_id": 101,
  "technician_id": 1001,
  "from_date": "2026-01-01",
  "to_date": "2026-01-31"
}
```

### Response 200

```json
{
  "center_id": 101,
  "technicians": [
    {
      "technician_id": 1001,
      "technician_name": "Kỹ thuật viên 1001",
      "csat_score": 88.5,
      "nps_score": 50
    }
  ]
}
```

### HTTP Status

| Status | Meaning |
|---|---|
| 200 | Lấy dữ liệu thành công |
| 400 | Tham số không hợp lệ |
| 404 | Không tìm thấy kỹ thuật viên hoặc dữ liệu |
| 409 | Xung đột dữ liệu |

---

# 5. Endpoint 4 – Xem báo cáo tổng hợp

## GET /api/csat-nps/summary

### User Story

US5 – Xem báo cáo tổng hợp.

### Mục đích

Lấy báo cáo CSAT/NPS tổng hợp trên toàn công ty
để Ban giám đốc theo dõi chất lượng dịch vụ.

### Request

#### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| from_date | date | Yes | Ngày bắt đầu |
| to_date | date | Yes | Ngày kết thúc |

### Request mẫu

```json
{
  "from_date": "2026-01-01",
  "to_date": "2026-01-31"
}
```

### Response 200

```json
{
  "from_date": "2026-01-01",
  "to_date": "2026-01-31",
  "total_surveys": 500,
  "csat_score": 85.5,
  "nps_score": 42
}
```

### HTTP Status

| Status | Meaning |
|---|---|
| 200 | Lấy báo cáo thành công |
| 400 | Khoảng thời gian không hợp lệ |
| 404 | Không có dữ liệu báo cáo |
| 409 | Xung đột dữ liệu |

---

# 6. Endpoint 5 – Kiểm tra phạm vi dữ liệu

## GET /api/csat-nps/access-scope

### User Story

US7 – Kiểm soát phạm vi dữ liệu.

### Mục đích

Xác định phạm vi trung tâm mà người dùng được phép
truy cập trước khi trả về dữ liệu CSAT/NPS.

### Request

#### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | integer | Yes | Mã trung tâm cần kiểm tra |

### Request mẫu

```json
{
  "center_id": 101
}
```

### Response 200

```json
{
  "center_id": 101,
  "allowed": true
}
```

### HTTP Status

| Status | Meaning |
|---|---|
| 200 | Kiểm tra quyền thành công |
| 400 | Mã trung tâm không hợp lệ |
| 404 | Không tìm thấy trung tâm |
| 409 | Xung đột phạm vi phân quyền |

---

# 7. Endpoint 6 – Hiển thị thông tin khách hàng đã che số điện thoại

## GET /api/csat-nps/customers/{customer_id}

### User Story

US8 – Che số điện thoại khách hàng.

### Mục đích

Trả về thông tin khách hàng trong đó số điện thoại
được che nhằm bảo vệ thông tin cá nhân.

### Request

#### Path Parameter

| Parameter | Type | Required | Description |
|---|---|---|---|
| customer_id | integer | Yes | Mã khách hàng |

### Request mẫu

```json
{
  "customer_id": 10001
}
```

### Response 200

```json
{
  "customer_id": 10001,
  "customer_name": "Khách hàng 10001",
  "phone": "090****567"
}
```

### HTTP Status

| Status | Meaning |
|---|---|
| 200 | Lấy thông tin thành công |
| 400 | Mã khách hàng không hợp lệ |
| 404 | Không tìm thấy khách hàng |
| 409 | Xung đột dữ liệu khách hàng |

---

# 8. Bảng validation

| Field | Bắt buộc | Kiểu dữ liệu | Quy tắc |
|---|---|---|---|
| from_date | Có | date | Đúng định dạng YYYY-MM-DD |
| to_date | Có | date | Đúng định dạng YYYY-MM-DD và không nhỏ hơn from_date |
| center_id | Tùy endpoint | integer | Phải là số nguyên dương |
| technician_id | Không | integer | Nếu có phải là số nguyên dương |
| customer_id | Có | integer | Phải là số nguyên dương |
| phone | Có trong response | string | Phải được che khi hiển thị |

---

# 9. Traceability – Endpoint với User Story

| Endpoint | User Story | MoSCoW |
|---|---|---|
| GET /api/csat-nps/time | US1 | MUST |
| GET /api/csat-nps/centers | US2, US3, US7 | MUST |
| GET /api/csat-nps/technicians | US4, US7 | MUST |
| GET /api/csat-nps/summary | US5 | MUST |
| GET /api/csat-nps/access-scope | US7 | MUST |
| GET /api/csat-nps/customers/{customer_id} | US8 | MUST |

## Tự kiểm

- US1 → GET /api/csat-nps/time
- US2 → GET /api/csat-nps/centers
- US3 → GET /api/csat-nps/centers
- US4 → GET /api/csat-nps/technicians
- US5 → GET /api/csat-nps/summary
- US7 → GET /api/csat-nps/access-scope và cơ chế kiểm soát trên các endpoint dữ liệu
- US8 → GET /api/csat-nps/customers/{customer_id}

US6 – SHOULD – không thuộc phạm vi endpoint MUST của Track SE.
