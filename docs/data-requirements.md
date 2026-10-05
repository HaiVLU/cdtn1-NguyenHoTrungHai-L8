# Data Requirement Spec – L8 CSAT/NPS

## 1. Mục tiêu

Dữ liệu phục vụ luồng L8 – Hệ thống CSAT/NPS của Mekong Mobile nhằm hỗ trợ:

- Xem CSAT/NPS theo thời gian.
- Xem CSAT/NPS theo trung tâm.
- Xem CSAT/NPS theo kỹ thuật viên.
- Xem báo cáo CSAT/NPS tổng hợp.
- Phân tích kết quả khảo sát hài lòng của khách hàng.
- Kiểm soát phạm vi dữ liệu theo trung tâm.
- Bảo vệ thông tin cá nhân của khách hàng.

---

## 2. Bảng nguồn dữ liệu

| Tệp | Số dòng | Nội dung | Dùng cho luồng |
|---|---:|---|---|
| customers_raw.csv | ~65.000 | Hồ sơ khách hàng thô, có trùng lặp, sai định dạng số điện thoại, tên viết hoa/thường lẫn lộn | L1, L7, L9 |
| orders_2024_2026.csv | ~26.000 | Đơn hàng 26 tháng của 24 cửa hàng, có 3 định dạng ngày lẫn lộn | L3, L6, L9 |
| order_items.csv | ~48.000 | Dòng hàng của các đơn, có vài dòng `thanh_tien` không khớp `so_luong × don_gia` | L6 |
| products.csv | 420 | Danh mục sản phẩm, có tên viết theo nhiều cách khác nhau | L6, L10 |
| stores.csv | 24 | Danh sách cửa hàng kèm thành phố và ngày khai trương | L6 |
| service_centers.csv | 6 | Danh sách trung tâm bảo hành | L2, L4, L5 |
| technicians.csv | 38 | Kỹ thuật viên kèm bậc tay nghề và trung tâm làm việc | L4 |
| technician_skills.csv | 152 | Tay nghề của kỹ thuật viên theo từng nhóm sự cố | L4 |
| tickets_history.csv | ~7.800 | Phiếu bảo hành lịch sử 30 tháng, đã có nhóm sự cố gán nhãn | L2, L4, L8, L10 |
| ticket_status_log.csv | ~31.000 | Lịch sử chuyển trạng thái của các phiếu | L2, L4, L8 |
| issue_descriptions.csv | 4.000 | Mô tả lỗi bằng văn bản tự do, đã gán nhãn nhóm sự cố | L10 |
| parts.csv | 180 | Danh mục linh kiện kèm đơn giá | L5 |
| part_transactions.csv | ~9.400 | Nhập – xuất linh kiện theo trung tâm | L5 |
| survey_responses.csv | ~2.600 | Phản hồi khảo sát hài lòng kèm điểm và nhận xét | L8 |

---

## 3. Nguồn dữ liệu chính cho L8

Nguồn dữ liệu chính phục vụ phân tích CSAT/NPS là:

### survey_responses.csv

- Số dòng: khoảng 2.600.
- Nội dung: phản hồi khảo sát hài lòng của khách hàng.
- Có điểm đánh giá và nhận xét.
- Là nguồn dữ liệu chính để tính toán và phân tích CSAT/NPS.

### tickets_history.csv

- Số dòng: khoảng 7.800.
- Nội dung: phiếu bảo hành lịch sử 30 tháng.
- Đã có nhóm sự cố được gán nhãn.
- Dùng để liên kết kết quả khảo sát với phiếu bảo hành.

### ticket_status_log.csv

- Số dòng: khoảng 31.000.
- Nội dung: lịch sử chuyển trạng thái của phiếu.
- Dùng để xác định trạng thái và lịch sử xử lý phiếu.

### service_centers.csv

- Số dòng: 6.
- Nội dung: danh sách trung tâm bảo hành.
- Dùng để xác định trung tâm của dữ liệu khảo sát và phiếu bảo hành.

### technicians.csv

- Số dòng: 38.
- Nội dung: danh sách kỹ thuật viên, bậc tay nghề và trung tâm làm việc.
- Dùng để phân tích CSAT/NPS theo kỹ thuật viên.

### customers_raw.csv

- Số dòng: khoảng 65.000.
- Nội dung: hồ sơ khách hàng.
- Có trùng lặp và sai định dạng số điện thoại.
- Dùng khi cần liên kết thông tin khách hàng và thực hiện quy tắc bảo vệ thông tin cá nhân.

---

## 4. Data Dictionary

### 4.1. survey_responses.csv

| Tên trường | Kiểu dữ liệu dự kiến | Ý nghĩa | Quy tắc/giá trị hợp lệ |
|---|---|---|---|
| survey_id | INT | Mã khảo sát | Không trùng |
| ticket_id | INT | Mã phiếu bảo hành liên quan | Phải tồn tại trong tickets_history |
| customer_id | INT | Mã khách hàng | Phải tồn tại trong dữ liệu khách hàng |
| center_id | INT | Mã trung tâm | Phải tồn tại trong service_centers |
| technician_id | INT | Mã kỹ thuật viên | Phải tồn tại trong technicians nếu có |
| survey_date | DATE | Ngày thực hiện khảo sát | Ngày hợp lệ |
| csat_score | DECIMAL/INT | Điểm CSAT | Theo thang điểm của khảo sát |
| nps_score | INT | Điểm NPS | 0–10 nếu sử dụng thang NPS |
| comment | TEXT | Nhận xét của khách hàng | Có thể rỗng |

---

### 4.2. tickets_history.csv

| Tên trường | Ý nghĩa | Quy tắc |
|---|---|---|
| ticket_id | Mã phiếu bảo hành | Duy nhất |
| customer_id | Khách hàng | Phải tham chiếu khách hàng hợp lệ |
| center_id | Trung tâm xử lý | Phải tồn tại trong service_centers |
| technician_id | Kỹ thuật viên xử lý | Phải tồn tại trong technicians nếu có |
| issue_group | Nhóm sự cố | Đã được gán nhãn |
| ticket_status | Trạng thái phiếu | Theo vòng đời phiếu |
| created_at | Thời điểm tạo phiếu | Ngày giờ hợp lệ |
| closed_at | Thời điểm đóng phiếu | Không nhỏ hơn created_at |

---

### 4.3. service_centers.csv

| Tên trường | Ý nghĩa | Quy tắc |
|---|---|---|
| center_id | Mã trung tâm | Duy nhất |
| center_name | Tên trung tâm | Không rỗng |

---

### 4.4. technicians.csv

| Tên trường | Ý nghĩa | Quy tắc |
|---|---|---|
| technician_id | Mã kỹ thuật viên | Duy nhất |
| technician_name | Tên kỹ thuật viên | Không rỗng |
| skill_level | Bậc tay nghề | Giá trị hợp lệ theo hệ thống |
| center_id | Trung tâm làm việc | Phải tồn tại trong service_centers |

---

### 4.5. customers_raw.csv

| Tên trường | Ý nghĩa | Quy tắc |
|---|---|---|
| customer_id | Mã khách hàng | Duy nhất sau xử lý |
| customer_name | Tên khách hàng | Chuẩn hóa chữ hoa/thường |
| phone | Số điện thoại | Chuẩn hóa định dạng |
| ... | Các thuộc tính khách hàng khác | Theo dữ liệu thực tế |

**Lưu ý chất lượng dữ liệu:**

- Có hồ sơ khách hàng bị trùng lặp.
- Có số điện thoại sai định dạng.
- Tên khách hàng có cách viết hoa/thường không đồng nhất.

---

## 5. Quy tắc chất lượng dữ liệu

### DQ1 – Completeness

Các trường bắt buộc của dữ liệu khảo sát phải có giá trị.

Mục tiêu:

> Completeness ≥ 95%

Các trường cần kiểm tra gồm:

- survey_id
- ticket_id
- customer_id
- center_id
- survey_date
- csat_score
- nps_score

Tỷ lệ thiếu thực tế cần được tính trực tiếp trên `survey_responses.csv`.

---

### DQ2 – Uniqueness

Mỗi khảo sát phải được xác định duy nhất bằng `survey_id`.

Không được có hai bản ghi khảo sát cùng `survey_id`.

Ngoài ra, mỗi phiếu chỉ được ghi nhận khảo sát một lần theo QT-10.

---

### DQ3 – Referential Integrity

Các khóa tham chiếu phải tồn tại:

- `survey_responses.ticket_id`
  → `tickets_history.ticket_id`

- `survey_responses.customer_id`
  → khách hàng hợp lệ

- `survey_responses.center_id`
  → `service_centers.center_id`

- `survey_responses.technician_id`
  → `technicians.technician_id`

---

### DQ4 – Data Consistency

Thông tin trung tâm và kỹ thuật viên phải nhất quán.

Ví dụ:

Kỹ thuật viên được gán cho trung tâm A không được xuất hiện như kỹ thuật viên thuộc trung tâm B trong cùng một ngữ cảnh dữ liệu.

---

### DQ5 – Customer Data Quality

Dữ liệu từ `customers_raw.csv` cần được kiểm tra:

- Trùng hồ sơ khách hàng.
- Số điện thoại sai định dạng.
- Tên viết hoa/thường không đồng nhất.

Các vấn đề này phải được xử lý trước khi sử dụng dữ liệu khách hàng cho phân tích.

---

### DQ6 – Customer Privacy

Số điện thoại khách hàng không được hiển thị đầy đủ trên báo cáo.

Ví dụ:

```text
0901234567 → 090****567
