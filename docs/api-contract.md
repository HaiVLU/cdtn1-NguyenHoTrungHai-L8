# API Contract – Track SE
## Luồng L8: Khảo sát hài lòng CSAT/NPS – Smart CRM Mekong Mobile

- **Phiên bản:** 1.0
- **Trạng thái:** Đặc tả API cho BT1 – Phân tích và Thiết kế; chưa phải mã triển khai.
- **Phạm vi:** Chỉ đọc và tổng hợp báo cáo khảo sát hài lòng sau khi phiếu bảo hành được đóng.
- **Đối tượng sử dụng:** Marketing, Quản lý trung tâm bảo hành, Ban giám đốc.

---

## 1. Quy ước chung

### 1.1. Base path và định dạng

- Base path: `/api/v1`
- Các endpoint trong tài liệu đều là HTTP `GET`, chỉ phục vụ truy vấn báo cáo.
- Request/response dùng JSON và UTF-8.
- Ngày truyền theo định dạng `YYYY-MM-DD`.
- Khoảng thời gian được tính từ `startDate` đến hết `endDate` theo ngày lịch.
- Các endpoint yêu cầu người dùng đã đăng nhập. Cơ chế cấp token cụ thể thuộc phạm vi triển khai ở BT2, không được quy định chi tiết trong BT1.

### 1.2. Quy ước thuật ngữ

| Thuật ngữ nghiệp vụ | Tên kỹ thuật sử dụng trong API | Ý nghĩa |
|---|---|---|
| Khảo sát hài lòng | `survey_response` | Phản hồi của khách hàng sau khi phiếu bảo hành được đóng |
| Phiếu bảo hành | `ticket` | Hồ sơ bảo hành liên kết với khảo sát |
| Trung tâm bảo hành | `service_center` | Trung tâm phụ trách phiếu bảo hành |
| Kỹ thuật viên | `technician` | Nhân viên thực hiện bảo hành |
| Khách hàng | `customer` | Khách hàng có phản hồi khảo sát |
| Ngày khảo sát | `responded_at` / `DIM_DATE` | Thời điểm phản hồi, dùng để lọc và tổng hợp theo thời gian |

### 1.3. Vai trò và phạm vi dữ liệu

| Vai trò | Quyền trong luồng L8 |
|---|---|
| Marketing | Xem báo cáo theo thời gian và so sánh giữa các trung tâm |
| Quản lý trung tâm | Chỉ xem dữ liệu của trung tâm được phân quyền; được xem kết quả theo kỹ thuật viên thuộc trung tâm đó |
| Ban giám đốc | Xem báo cáo tổng hợp toàn công ty và lọc theo trung tâm/thời gian |

**Quy tắc bắt buộc:** Không tin `centerId` do client gửi lên nếu người dùng là Quản lý trung tâm. API phải lấy phạm vi trung tâm từ quyền đã xác thực ở phía server. Nếu người quản lý cố truy cập trung tâm khác, trả `403 Forbidden` và không trả dữ liệu của trung tâm đó.

### 1.4. Quy tắc nghiệp vụ liên quan

- Chỉ tính phản hồi hợp lệ gắn với phiếu bảo hành đã đóng.
- Mỗi phiếu bảo hành có tối đa một phản hồi khảo sát hợp lệ.
- Quản lý trung tâm chỉ xem dữ liệu trong phạm vi trung tâm được phân quyền; Ban giám đốc xem toàn công ty.
- Số điện thoại khách hàng phải được che khi hiển thị cho Quản lý trung tâm và Ban giám đốc.
- Không cung cấp API tạo, sửa hoặc xóa phiếu bảo hành/khách hàng trong phạm vi L8.

---

## 2. Danh sách endpoint

| Mã | Method và endpoint | Mục đích | User Story liên quan |
|---|---|---|---|
| API-01 | `GET /api/v1/reports/csat-nps/summary` | Xem báo cáo tổng hợp trong khoảng thời gian | US1, US5 |
| API-02 | `GET /api/v1/reports/csat-nps/trend` | Xem xu hướng theo ngày hoặc tháng | US1, US6 |
| API-03 | `GET /api/v1/reports/csat-nps/centers` | So sánh kết quả giữa các trung tâm | US2, US6 |
| API-04 | `GET /api/v1/reports/csat-nps/technicians` | Xem kết quả theo kỹ thuật viên trong phạm vi trung tâm | US3, US4, US7 |
| API-05 | `GET /api/v1/reports/csat-nps/centers/{centerId}` | Xem chi tiết báo cáo của một trung tâm | US2, US3, US6, US7 |

US6 có mức **SHOULD** trong SRS; các endpoint phục vụ US6 không làm thay đổi mức ưu tiên đã ghi trong SRS.

---

## 3. Đặc tả endpoint

### API-01 – Báo cáo tổng hợp

**Request**

`GET /api/v1/reports/csat-nps/summary?startDate=2026-09-01&endDate=2026-09-30`

| Tham số | Kiểu | Bắt buộc | Quy tắc |
|---|---|---|---|
| `startDate` | string, date | Có | Ngày bắt đầu hợp lệ |
| `endDate` | string, date | Có | Ngày kết thúc hợp lệ; không nhỏ hơn `startDate` |

**Response thành công – `200 OK`**

```json
{
  "data": {
    "period": {
      "startDate": "2026-09-01",
      "endDate": "2026-09-30"
    },
    "surveyCount": 120,
    "csat": {
      "averageScore": 4.2,
      "scoreScale": "1-5"
    },
    "nps": {
      "score": null,
      "status": "unavailable",
      "reason": "Nguồn dữ liệu hiện tại chưa có điểm giới thiệu theo thang 0-10."
    }
  },
  "message": "Report generated successfully."
}
```

`surveyCount` là số phản hồi khảo sát hợp lệ trong kỳ. `csat.averageScore` là điểm trung bình của trường `SURVEY_RESPONSE.score` (thang 1–5). Không được tự gọi điểm trung bình này là phần trăm CSAT.

`nps.score` để `null` cho đến khi mô hình dữ liệu có trường điểm giới thiệu 0–10 và nghiệp vụ xác định cách tính NPS. Không suy ra NPS từ điểm CSAT 1–5.

### API-02 – Xu hướng theo thời gian

**Request**

`GET /api/v1/reports/csat-nps/trend?startDate=2026-09-01&endDate=2026-09-30&groupBy=day`

| Tham số | Kiểu | Bắt buộc | Quy tắc |
|---|---|---|---|
| `startDate` | string, date | Có | Ngày bắt đầu hợp lệ |
| `endDate` | string, date | Có | Ngày kết thúc không trước ngày bắt đầu |
| `groupBy` | string | Không | `day` hoặc `month`; mặc định `month` |

**Response thành công – `200 OK`**

```json
{
  "data": {
    "groupBy": "day",
    "items": [
      {
        "period": "2026-09-01",
        "surveyCount": 12,
        "csat": {
          "averageScore": 4.1,
          "scoreScale": "1-5"
        },
        "nps": {
          "score": null,
          "status": "unavailable"
        }
      }
    ]
  },
  "message": "Report generated successfully."
}
```

`items` chứa các kỳ tổng hợp trong khoảng ngày đã chọn. Dữ liệu phải được lọc theo thời điểm phản hồi khảo sát (`responded_at` hoặc ngày liên kết trong `DIM_DATE`).

### API-03 – So sánh giữa các trung tâm

**Request**

`GET /api/v1/reports/csat-nps/centers?startDate=2026-09-01&endDate=2026-09-30`

**Response thành công – `200 OK`**

```json
{
  "data": {
    "period": {
      "startDate": "2026-09-01",
      "endDate": "2026-09-30"
    },
    "items": [
      {
        "centerId": 1,
        "centerName": "Trung tâm bảo hành Quận 10",
        "surveyCount": 35,
        "csat": {
          "averageScore": 4.3,
          "scoreScale": "1-5"
        },
        "nps": {
          "score": null,
          "status": "unavailable"
        }
      }
    ]
  },
  "message": "Report generated successfully."
}
```

Tên trung tâm trong ví dụ chỉ minh họa cấu trúc response, không phải dữ liệu thật đã được xác minh. Kết quả phải lấy từ `SERVICE_CENTER`, `TICKET` và `SURVEY_RESPONSE`. Với Quản lý trung tâm, server chỉ trả trung tâm được phân quyền; không dùng tham số client để mở rộng quyền.

### API-04 – Báo cáo theo kỹ thuật viên

**Request**

`GET /api/v1/reports/csat-nps/technicians?startDate=2026-09-01&endDate=2026-09-30`

| Tham số | Kiểu | Bắt buộc | Quy tắc |
|---|---|---|---|
| `startDate` | string, date | Có | Ngày bắt đầu hợp lệ |
| `endDate` | string, date | Có | Ngày kết thúc không trước ngày bắt đầu |
| `centerId` | integer | Không | Chỉ dùng để lọc khi vai trò được phép; với Quản lý trung tâm, phạm vi thực tế lấy từ quyền phía server |

**Response thành công – `200 OK`**

```json
{
  "data": {
    "period": {
      "startDate": "2026-09-01",
      "endDate": "2026-09-30"
    },
    "centerId": 1,
    "items": [
      {
        "technicianId": 12,
        "technicianName": "Nguyễn Văn A",
        "surveyCount": 8,
        "csat": {
          "averageScore": 4.5,
          "scoreScale": "1-5"
        },
        "nps": {
          "score": null,
          "status": "unavailable"
        }
      }
    ]
  },
  "message": "Report generated successfully."
}
```

Tên kỹ thuật viên trong ví dụ chỉ minh họa định dạng, không phải dữ liệu thật đã được xác minh. Dữ liệu phải được tổng hợp theo `TICKET.technician_id` và chỉ gồm phiếu/khảo sát hợp lệ của trung tâm được phép truy cập.

### API-05 – Báo cáo chi tiết theo trung tâm

**Request**

`GET /api/v1/reports/csat-nps/centers/1?startDate=2026-09-01&endDate=2026-09-30`

**Response thành công – `200 OK`**

```json
{
  "data": {
    "center": {
      "centerId": 1,
      "centerName": "Trung tâm bảo hành Quận 10"
    },
    "period": {
      "startDate": "2026-09-01",
      "endDate": "2026-09-30"
    },
    "surveyCount": 35,
    "csat": {
      "averageScore": 4.3,
      "scoreScale": "1-5"
    },
    "nps": {
      "score": null,
      "status": "unavailable"
    }
  },
  "message": "Report generated successfully."
}
```

Nếu `centerId` không tồn tại, trả `404 Not Found`. Nếu người dùng không có quyền xem trung tâm đó, trả `403 Forbidden` và không tiết lộ dữ liệu báo cáo.

---

## 4. Cấu trúc lỗi dùng chung

| HTTP status | Mã lỗi | Khi nào sử dụng |
|---|---|---|
| `400 Bad Request` | `INVALID_DATE_RANGE` | Thiếu ngày bắt buộc, ngày không hợp lệ hoặc `startDate > endDate` |
| `400 Bad Request` | `INVALID_GROUP_BY` | `groupBy` không phải `day` hoặc `month` |
| `401 Unauthorized` | `UNAUTHENTICATED` | Chưa đăng nhập hoặc thông tin xác thực không hợp lệ |
| `403 Forbidden` | `CENTER_SCOPE_FORBIDDEN` | Quản lý trung tâm yêu cầu dữ liệu ngoài phạm vi được phân quyền |
| `404 Not Found` | `CENTER_NOT_FOUND` | Không tìm thấy trung tâm được yêu cầu |
| `500 Internal Server Error` | `INTERNAL_ERROR` | Lỗi xử lý không dự kiến |

**Ví dụ lỗi ngày không hợp lệ – `400 Bad Request`**

```json
{
  "error": {
    "code": "INVALID_DATE_RANGE",
    "message": "Ngày bắt đầu phải nhỏ hơn hoặc bằng ngày kết thúc."
  }
}
```

**Ví dụ không có dữ liệu – `200 OK`**

```json
{
  "data": {
    "period": {
      "startDate": "2026-09-01",
      "endDate": "2026-09-30"
    },
    "surveyCount": 0,
    "items": []
  },
  "message": "Không có dữ liệu khảo sát."
}
```

Trường hợp không có dữ liệu là kết quả truy vấn hợp lệ, không phải lỗi máy chủ.

---

## 5. Quy tắc dữ liệu và bảo mật

1. **Nguồn dữ liệu:** `CUSTOMER`, `SERVICE_CENTER`, `TECHNICIAN`, `TICKET`, `SURVEY_RESPONSE`, `DIM_DATE` theo mô hình dữ liệu BT1 hiện tại.
2. **Điều kiện khảo sát hợp lệ:** Chỉ tổng hợp phản hồi gắn với phiếu bảo hành đã đóng. Mỗi `ticket_id` có tối đa một phản hồi hợp lệ; mô hình hiện tại thể hiện ràng buộc này bằng `UNIQUE` trên `SURVEY_RESPONSE.ticket_id`.
3. **Lọc thời gian:** Lọc theo thời điểm phản hồi (`responded_at`) hoặc ngày khảo sát liên kết với `DIM_DATE`; chọn một cách triển khai thống nhất ở BT2.
4. **Phân quyền:** Kiểm tra quyền trước khi truy vấn/trả báo cáo. Quản lý trung tâm chỉ xem trung tâm được gán; Ban giám đốc được xem toàn công ty; Marketing xem báo cáo theo phạm vi chức năng trong SRS.
5. **Che số điện thoại:** Nếu response có chứa số điện thoại, phải masking theo QT-15/NFR4 đối với Quản lý trung tâm và Ban giám đốc. Các endpoint tổng hợp trong tài liệu này không cần trả số điện thoại, vì vậy ưu tiên không đưa trường này vào response.
6. **Không xóa lịch sử:** Các API báo cáo không xóa dữ liệu khảo sát hoặc phiếu bảo hành.
7. **Hiệu năng:** Mục tiêu SRS NFR1 là phản hồi không quá 2 giây với tối đa 10.000 bản ghi khảo sát. Đây là ngưỡng cần kiểm chứng khi triển khai, không phải cam kết hiệu năng đã đo ở BT1.
8. **Không trả dữ liệu ngoài phạm vi:** Khi từ chối truy cập, response không được chứa tên, số liệu hoặc thông tin của trung tâm không được phép xem.

---

## 6. Ánh xạ API với SRS và mô hình dữ liệu

| Yêu cầu | API liên quan | Dữ liệu chính |
|---|---|---|
| FR1 / US1 – Xem CSAT/NPS theo thời gian | API-01, API-02 | `SURVEY_RESPONSE.responded_at`, `DIM_DATE`, `SURVEY_RESPONSE.score` |
| FR2 / US2 – So sánh theo trung tâm | API-03, API-05 | `SERVICE_CENTER`, `TICKET.center_id`, `SURVEY_RESPONSE` |
| FR3 / US3 – Quản lý xem dữ liệu trung tâm mình | API-04, API-05 | `SERVICE_CENTER`, quyền trung tâm, `TICKET.center_id` |
| FR4 / US4 – Xem theo kỹ thuật viên | API-04 | `TECHNICIAN`, `TICKET.technician_id`, `SURVEY_RESPONSE` |
| FR5 / US5 – Báo cáo tổng hợp toàn công ty | API-01 | `SURVEY_RESPONSE`, `TICKET`, `SERVICE_CENTER` |
| FR6 / US6 – Ban giám đốc lọc theo trung tâm/thời gian (SHOULD) | API-02, API-03, API-05 | `DIM_DATE`, `SERVICE_CENTER`, `TICKET`, `SURVEY_RESPONSE` |
| FR7 / US7 – Giới hạn phạm vi Quản lý trung tâm | API-03, API-04, API-05 | Quyền người dùng và `TICKET.center_id` |
| QT-15 / NFR4 – Che số điện thoại | Tất cả API có trả dữ liệu khách hàng | `CUSTOMER.phone`; ưu tiên không trả trường này trong báo cáo tổng hợp |

---

## 7. Điểm cần thống nhất trước khi triển khai NPS

Case study Mekong Mobile mô tả `survey_response` là phản hồi sau khi phiếu bảo hành đóng, có thang điểm **1–5 kèm nhận xét**. ERD/DDL hiện tại của bài BT1 cũng chỉ có `SURVEY_RESPONSE.score SMALLINT` với ràng buộc `1 <= score <= 5`. Dữ liệu này hỗ trợ thống kê điểm khảo sát thang 1–5, nhưng **không đủ để tính NPS chuẩn**, vốn cần câu hỏi giới thiệu theo thang 0–10 và phân loại người trả lời.

Vì SRS của luồng L8 đang yêu cầu CSAT/NPS, cần chọn và thống nhất một trong hai hướng trước BT2:

- **Hướng A – Giữ nguyên dữ liệu case study:** Báo cáo điểm khảo sát thang 1–5; NPS trả `null`/`unavailable` cho tới khi có nguồn điểm NPS. Cần hỏi giảng viên xem cách này có đáp ứng phạm vi L8 đã duyệt không.
- **Hướng B – Bổ sung dữ liệu NPS có chủ đích:** Được giảng viên chấp thuận rồi bổ sung trường `nps_score` (0–10) hoặc cấu trúc dữ liệu khảo sát phù hợp; cập nhật ERD, SQL DDL, mô tả bảng và API Contract đồng bộ. Không được chỉ thêm trường trong API mà không cập nhật mô hình dữ liệu.

Không tự chuyển `score` 1–5 thành NPS 0–10 vì sẽ làm sai ý nghĩa dữ liệu nguồn.

---

## 8. Giới hạn của tài liệu BT1

Tài liệu này mô tả hợp đồng API ở mức phân tích và thiết kế: endpoint, tham số, cấu trúc response, lỗi, phân quyền, nguồn dữ liệu và truy vết yêu cầu. Đây **không phải** mã nguồn API đã triển khai; chưa khẳng định endpoint tồn tại hoặc hiệu năng đã được kiểm thử. Việc xác định cơ chế xác thực cụ thể, công nghệ backend, truy vấn SQL và kiểm thử thực tế thuộc giai đoạn triển khai tiếp theo.
