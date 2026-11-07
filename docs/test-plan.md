# TEST PLAN – SMART CRM MEKONG MOBILE (L8)

## 1. Mục tiêu
Kiểm tra tính hợp lệ của dữ liệu khảo sát CSAT/NPS và các quy tắc nghiệp vụ QT-10 đang được triển khai trong `src/services/survey_service.py`.

## 2. Phạm vi
- Hàm `validate(data)`: cấu trúc JSON object, trường bắt buộc, kiểu dữ liệu, miền giá trị CSAT 1–5, NPS 0–10 và comment.
- Hàm `validate_business_rules(...)`: ticket tồn tại, ticket đã đóng, ngày khảo sát tồn tại, không tạo khảo sát trùng; cho phép cập nhật chính bản ghi hiện tại.
- Kiểm tra tính ổn định của kết quả xác thực khi chạy lặp lại.

## 3. Ngoài phạm vi / giới hạn
- Bộ test hiện tại là unit test, dùng mock repository cho các quy tắc nghiệp vụ; không ghi dữ liệu vào PostgreSQL thật.
- Chưa kiểm thử tích hợp toàn bộ CRUD API, giao diện React, hiệu năng, CORS, xác thực đăng nhập hoặc phân quyền người dùng.
- Chưa có cơ chế xác thực/phân quyền hoàn chỉnh trong source được cung cấp; không tuyên bố đã kiểm thử bảo mật phân quyền.
- Kiểm thử NPS chỉ kiểm tra miền điểm 0–10, không xác nhận cách tính chỉ số NPS chuẩn.

## 4. Môi trường
- Python theo `requirements.txt` (source ban đầu dùng Python 3.13.5).
- pytest 9.x.
- Chạy từ thư mục gốc repository, trong môi trường `.venv` đã cài `requirements.txt`.

## 5. Danh sách test case

| ID | Nhóm | Nội dung / dữ liệu kiểm tra | Kết quả mong đợi |
|---|---|---|---|
| TC01 | Positive | Khảo sát hợp lệ đầy đủ trường | Chấp nhận |
| TC02 | Positive | Không truyền comment | Chấp nhận |
| TC03 | Positive | comment = null | Chấp nhận |
| TC04 | Boundary | CSAT = 1 | Chấp nhận |
| TC05 | Boundary | CSAT = 5 | Chấp nhận |
| TC06 | Boundary | NPS = 0 | Chấp nhận |
| TC07 | Boundary | NPS = 10 | Chấp nhận |
| TC08 | Negative | Body = null/list/string/số | Báo ValidationError |
| TC09 | Negative | Thiếu ticket_id | Báo thiếu trường |
| TC10 | Negative | Thiếu date_id | Báo thiếu trường |
| TC11 | Negative | Thiếu score | Báo thiếu trường |
| TC12 | Negative | Thiếu nps_score | Báo thiếu trường |
| TC13 | Negative | ticket_id/date_id/score/nps_score sai kiểu số nguyên | Báo sai kiểu |
| TC14 | Negative | ticket_id = 0 hoặc âm | Báo không hợp lệ |
| TC15 | Negative | date_id = 0 | Báo không hợp lệ |
| TC16 | Negative | CSAT = 0, 6 hoặc -1 | Báo ngoài miền 1–5 |
| TC17 | Negative | NPS = -1 hoặc 11 | Báo ngoài miền 0–10 |
| TC18 | Negative | comment là số | Báo sai kiểu |
| TC19 | Data quality | Ticket không tồn tại | Từ chối |
| TC20 | Data quality | Ticket ở trạng thái OPEN/PENDING/IN_PROGRESS | Từ chối |
| TC21 | Data quality | Ticket có trạng thái “Đã đóng” | Chấp nhận |
| TC22 | Data quality | date_id không tồn tại | Từ chối |
| TC23 | Data quality | Ticket đã có khảo sát (kể cả khảo sát soft-delete theo repository) | Từ chối |
| TC24 | Business rule | Cập nhật chính khảo sát hiện tại | Chấp nhận |
| TC25 | Reproducibility | Cùng dữ liệu hợp lệ được xác thực hai lần | Kết quả giống nhau |

**Lưu ý số lượng:** Pytest mở rộng các trường hợp `parametrize` thành nhiều lần chạy. Tổng số test case được thu thập là 38, không phải 25 dòng mô tả ở bảng.

## 6. Cách thực thi
```powershell
# Tại thư mục gốc repository, sau khi kích hoạt .venv
python -m pytest -o pythonpath=. -v
```

## 7. Tiêu chí hoàn thành
- Tất cả test case trong phạm vi chạy thành công (PASS).
- Không có lỗi thu thập test (collection error).
- Lưu ảnh chụp kết quả chạy thật vào `docs/screenshots/`.
- Ghi số PASS/FAIL theo kết quả pytest thực tế, không điền trước hoặc tự suy đoán.
