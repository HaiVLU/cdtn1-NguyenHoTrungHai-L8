# Data Requirement Spec – L8 CSAT/NPS

## 1. Mục tiêu

Dữ liệu phục vụ hệ thống CSAT/NPS của Mekong Mobile, nhằm hỗ trợ:

- Theo dõi CSAT/NPS theo thời gian.
- So sánh CSAT/NPS giữa các trung tâm.
- Theo dõi CSAT/NPS theo kỹ thuật viên.
- Xem báo cáo CSAT/NPS tổng hợp trên toàn công ty.
- Kiểm soát phạm vi dữ liệu theo trung tâm được phân quyền.
- Bảo vệ thông tin cá nhân của khách hàng khi hiển thị báo cáo.

Phạm vi dữ liệu chính gồm kết quả khảo sát CSAT/NPS,
phiếu bảo hành, trung tâm, kỹ thuật viên và thời gian.

---

# 2. Bảng nguồn dữ liệu

| Nguồn dữ liệu | Nội dung | Định dạng | Tần suất cập nhật | Khối lượng ước tính |
|---|---|---|---|---|
| Hệ thống CRM | Phiếu bảo hành, thông tin khách hàng, trung tâm và kỹ thuật viên | CSDL/API | Theo phát sinh giao dịch | Theo số lượng phiếu bảo hành |
| Dữ liệu khảo sát CSAT/NPS | Kết quả khảo sát và điểm CSAT/NPS | CSDL/API | Theo phát sinh khảo sát | Theo số lượng khảo sát hợp lệ |

> Ghi chú: Định dạng, tần suất và khối lượng cần được xác nhận lại
> với dữ liệu triển khai thực tế. Các giá trị trên là đặc tả ở mức
> yêu cầu dữ liệu cho BT1, không phải số liệu đo thực tế.

---

# 3. Data Dictionary

## 3.1 Fact_Survey

Một dòng trong Fact_Survey đại diện cho một kết quả khảo sát
hợp lệ của một phiếu bảo hành đã đóng.

| Tên cột | Kiểu dữ liệu | Ý nghĩa | Giá trị hợp lệ | Tỷ lệ thiếu |
|---|---|---|---|---|
| survey_id | INT | Mã khảo sát | Số nguyên dương, duy nhất | Chưa đo |
| ticket_id | INT | Mã phiếu bảo hành | Số nguyên dương | Chưa đo |
| date_key | INT | Khóa ngày khảo sát | Tham chiếu Dim_Date | Chưa đo |
| center_key | INT | Khóa trung tâm | Tham chiếu Dim_Center | Chưa đo |
| technician_key | INT | Khóa kỹ thuật viên | Tham chiếu Dim_Technician | Chưa đo |
| csat_score | DECIMAL | Điểm CSAT | Giá trị điểm CSAT hợp lệ theo quy định khảo sát | Chưa đo |
| nps_score | INT | Điểm NPS | Giá trị từ 0 đến 10 | Chưa đo |

---

## 3.2 Dim_Date

| Tên cột | Kiểu dữ liệu | Ý nghĩa | Giá trị hợp lệ | Tỷ lệ thiếu |
|---|---|---|---|---|
| date_key | INT | Khóa ngày | Số nguyên duy nhất | Chưa đo |
| full_date | DATE | Ngày đầy đủ | YYYY-MM-DD | Chưa đo |
| month | INT | Tháng | 1–12 | Chưa đo |
| quarter | INT | Quý | 1–4 | Chưa đo |
| year | INT | Năm | Năm hợp lệ | Chưa đo |

---

## 3.3 Dim_Center

| Tên cột | Kiểu dữ liệu | Ý nghĩa | Giá trị hợp lệ | Tỷ lệ thiếu |
|---|---|---|---|---|
| center_key | INT | Khóa trung tâm | Số nguyên duy nhất | Chưa đo |
| center_id | INT | Mã trung tâm | Số nguyên dương | Chưa đo |
| center_name | VARCHAR | Tên trung tâm | Chuỗi không rỗng | Chưa đo |

---

## 3.4 Dim_Technician

| Tên cột | Kiểu dữ liệu | Ý nghĩa | Giá trị hợp lệ | Tỷ lệ thiếu |
|---|---|---|---|---|
| technician_key | INT | Khóa kỹ thuật viên | Số nguyên duy nhất | Chưa đo |
| technician_id | INT | Mã kỹ thuật viên | Số nguyên dương | Chưa đo |
| technician_name | VARCHAR | Tên kỹ thuật viên | Chuỗi không rỗng | Chưa đo |
| center_key | INT | Trung tâm của kỹ thuật viên | Tham chiếu Dim_Center | Chưa đo |

---

# 4. Quy tắc chất lượng dữ liệu

## DQ1 – Completeness

Các trường dữ liệu bắt buộc của một kết quả khảo sát hợp lệ
phải có tỷ lệ đầy đủ tối thiểu:

**Completeness ≥ 95%.**

Các trường bắt buộc gồm:

- survey_id
- ticket_id
- date_key
- center_key
- technician_key
- csat_score
- nps_score

Nếu tỷ lệ completeness nhỏ hơn 95%, dữ liệu phải được cảnh báo
và xử lý trước khi sử dụng cho báo cáo chính thức.

---

## DQ2 – Không trùng theo khóa nghiệp vụ

Một phiếu bảo hành chỉ được ghi nhận tối đa một khảo sát hợp lệ.

Khóa nghiệp vụ kiểm tra trùng:

**ticket_id + survey_id**

Không cho phép xuất hiện hai bản ghi khảo sát hợp lệ
trùng cùng khóa nghiệp vụ.

Quy tắc này liên quan đến QT-10.

---

## DQ3 – Referential Integrity

Các khóa ngoại phải tồn tại trong bảng dimension tương ứng:

- date_key phải tồn tại trong Dim_Date.
- center_key phải tồn tại trong Dim_Center.
- technician_key phải tồn tại trong Dim_Technician.

Bản ghi không thỏa điều kiện tham chiếu không được sử dụng
để tính toán báo cáo chính thức.

---

## DQ4 – Data Scope

Dữ liệu CSAT/NPS trả về cho Quản lý trung tâm chỉ được thuộc
trung tâm mà người dùng được phân quyền.

Không cho phép Quản lý trung tâm xem dữ liệu của trung tâm khác.

Quy tắc này liên quan đến US7.

---

## DQ5 – Customer Privacy

Số điện thoại khách hàng phải được che khi hiển thị trên báo cáo.

Ví dụ:

**0901234567 → 090****567**

Không hiển thị đầy đủ số điện thoại khách hàng cho người dùng
không có quyền phù hợp.

Quy tắc này liên quan đến US8 và QT-15.

---

# 5. Câu hỏi phân tích và mức độ chi tiết

## AQ1 – CSAT/NPS theo thời gian

**Câu hỏi:**

CSAT/NPS thay đổi như thế nào theo thời gian?

**Mức độ chi tiết:**

- Ngày
- Tháng
- Quý
- Năm

**User Story:** US1 – MUST.

---

## AQ2 – CSAT/NPS theo trung tâm

**Câu hỏi:**

CSAT/NPS của từng trung tâm là bao nhiêu và trung tâm nào
có kết quả cao hoặc thấp?

**Mức độ chi tiết:**

- Trung tâm
- Khoảng thời gian

**User Story:** US2 – MUST.

---

## AQ3 – CSAT/NPS của trung tâm quản lý

**Câu hỏi:**

Quản lý trung tâm đang phụ trách có thể xem CSAT/NPS
của trung tâm mình như thế nào?

**Mức độ chi tiết:**

- Trung tâm được phân quyền
- Khoảng thời gian

**User Story:** US3 – MUST.

---

## AQ4 – CSAT/NPS theo kỹ thuật viên

**Câu hỏi:**

CSAT/NPS của từng kỹ thuật viên trong trung tâm là bao nhiêu?

**Mức độ chi tiết:**

- Trung tâm
- Kỹ thuật viên
- Khoảng thời gian

**User Story:** US4 – MUST.

---

## AQ5 – Báo cáo CSAT/NPS tổng hợp

**Câu hỏi:**

CSAT/NPS tổng thể của toàn công ty là bao nhiêu?

**Mức độ chi tiết:**

- Toàn công ty
- Khoảng thời gian

**User Story:** US5 – MUST.

---

## AQ6 – CSAT/NPS theo trung tâm và thời gian

**Câu hỏi:**

CSAT/NPS của từng trung tâm thay đổi như thế nào theo thời gian?

**Mức độ chi tiết:**

- Trung tâm
- Ngày/Tháng/Quý/Năm

**User Story:** US6 – SHOULD.

---

# 6. Traceability – Câu hỏi phân tích với User Story

| Mã câu hỏi | Câu hỏi phân tích | User Story | MoSCoW |
|---|---|---|---|
| AQ1 | CSAT/NPS thay đổi theo thời gian như thế nào? | US1 | MUST |
| AQ2 | CSAT/NPS của từng trung tâm là bao nhiêu? | US2 | MUST |
| AQ3 | Quản lý xem CSAT/NPS của trung tâm mình như thế nào? | US3 | MUST |
| AQ4 | CSAT/NPS của từng kỹ thuật viên là bao nhiêu? | US4 | MUST |
| AQ5 | CSAT/NPS tổng thể toàn công ty là bao nhiêu? | US5 | MUST |
| AQ6 | CSAT/NPS từng trung tâm thay đổi theo thời gian như thế nào? | US6 | SHOULD |

## Tự kiểm

- AQ1 → US1: Có truy vết.
- AQ2 → US2: Có truy vết.
- AQ3 → US3: Có truy vết.
- AQ4 → US4: Có truy vết.
- AQ5 → US5: Có truy vết.
- AQ6 → US6: Có truy vết.

Không có câu hỏi phân tích nào không có User Story tương ứng.
