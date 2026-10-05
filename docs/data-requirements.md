# Data Requirements – L8 CSAT/NPS

## 1. Mục tiêu dữ liệu

Dữ liệu phục vụ phân tích mức độ hài lòng của khách hàng
thông qua CSAT/NPS theo:

- Thời gian
- Trung tâm
- Kỹ thuật viên

Dữ liệu được sử dụng để tạo báo cáo và hỗ trợ đánh giá
chất lượng dịch vụ.

## 2. Data Grain

Một dòng trong Fact_Survey đại diện cho một kết quả
khảo sát hợp lệ của một phiếu bảo hành đã đóng.

## 3. Fact Table

### Fact_Survey

| Field | Type | Description |
|---|---|---|
| survey_id | INT | Mã khảo sát |
| ticket_id | INT | Mã phiếu bảo hành |
| date_key | INT | Khóa ngày |
| center_key | INT | Khóa trung tâm |
| technician_key | INT | Khóa kỹ thuật viên |
| csat_score | DECIMAL | Điểm CSAT |
| nps_score | INT | Điểm NPS |

## 4. Dimension Tables

### Dim_Date

| Field | Type | Description |
|---|---|---|
| date_key | INT | Khóa ngày |
| full_date | DATE | Ngày đầy đủ |
| month | INT | Tháng |
| quarter | INT | Quý |
| year | INT | Năm |

### Dim_Center

| Field | Type | Description |
|---|---|---|
| center_key | INT | Khóa trung tâm |
| center_id | INT | Mã trung tâm |
| center_name | VARCHAR | Tên trung tâm |

### Dim_Technician

| Field | Type | Description |
|---|---|---|
| technician_key | INT | Khóa kỹ thuật viên |
| technician_id | INT | Mã kỹ thuật viên |
| technician_name | VARCHAR | Tên kỹ thuật viên |
| center_key | INT | Khóa trung tâm |

## 5. Data Quality Rules

### DQ1 – Uniqueness

Một phiếu bảo hành chỉ có tối đa một khảo sát hợp lệ.

Liên quan: QT-10 / NFR2.

### DQ2 – Completeness

Một bản ghi khảo sát hợp lệ phải có đầy đủ:

- survey_id
- ticket_id
- date_key
- center_key
- technician_key
- csat_score
- nps_score

### DQ3 – Referential Integrity

center_key và technician_key phải tham chiếu
đến dimension tương ứng.

### DQ4 – Access Scope

Dữ liệu trả về cho Quản lý trung tâm chỉ được thuộc
trung tâm mà người dùng được phân quyền.

Liên quan: QT-14 / NFR3.

### DQ5 – Customer Privacy

Số điện thoại khách hàng phải được masking khi hiển thị
cho Quản lý trung tâm và Ban giám đốc.

Liên quan: QT-15 / NFR4.
