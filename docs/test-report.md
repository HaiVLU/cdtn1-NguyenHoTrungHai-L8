# TEST REPORT – SMART CRM MEKONG MOBILE (L8)

## 1. Thông tin
- Module: Kiểm tra dữ liệu khảo sát CSAT/NPS và quy tắc QT-10.
- Framework: pytest.
- File kiểm thử: `tests/test_survey_validation.py`.
- Test Plan: [`test-plan.md`](test-plan.md).

## 2. Phạm vi đã xây dựng
Bộ test được mở rộng từ 5 lên **38 trường hợp pytest** (các ca tham số hóa được tính riêng), gồm:
- Positive: dữ liệu hợp lệ và comment tùy chọn.
- Boundary: CSAT ở hai đầu 1–5 và NPS ở hai đầu 0–10.
- Negative: body không phải object, thiếu trường, sai kiểu, ID không hợp lệ, điểm ngoài miền và comment sai kiểu.
- Chất lượng dữ liệu / quy tắc nghiệp vụ: ticket tồn tại và đã đóng, ngày khảo sát tồn tại, chống khảo sát trùng, cập nhật cùng bản ghi.
- Tái lập: cùng dữ liệu được xác thực lặp lại cho kết quả giống nhau.

## 3. Kết quả thực thi – cần cập nhật sau khi chạy trên máy dự án
**Không điền số PASS/FAIL trước khi thực thi bộ test mới.** Source được kiểm tra trong môi trường phân tích không có đủ các dependency Flask của dự án nên không thể xác nhận kết quả chạy tại đây.

Chạy lệnh sau trong Windows PowerShell tại thư mục gốc, khi `.venv` đã kích hoạt và dependencies đã cài:
```powershell
python -m pytest -o pythonpath=. -v
```

Sau khi chạy, cập nhật:
- Số test case đã chạy thật: ___
- PASS: ___
- FAIL: ___
- Thời gian: ___
- Kết quả tổng quát: ___

## 4. Đánh giá 5 nhóm
| Nhóm | Trạng thái sau khi bổ sung | Ghi chú |
|---|---|---|
| Luồng đúng (Positive) | Có test | Dữ liệu hợp lệ, comment tùy chọn |
| Biên (Boundary) | Có test | CSAT 1/5; NPS 0/10 |
| Dữ liệu sai (Negative) | Có test | Thiếu trường, sai kiểu, ngoài miền |
| Bảo mật/chất lượng dữ liệu | Có kiểm tra chất lượng dữ liệu | Kiểm tra QT-10 và chống trùng bằng mock; **chưa** kiểm thử xác thực/phân quyền hoặc bảo mật API |
| Tái lập (Reproducibility) | Có test cơ bản | So sánh kết quả xác thực lặp lại; chưa phải kiểm thử tái lập môi trường/database độc lập |

## 5. Giới hạn
- Các test nghiệp vụ dùng mock repository, không thay thế kiểm thử tích hợp PostgreSQL.
- Chưa có test client cho toàn bộ endpoint CRUD.
- Chưa có kiểm thử đăng nhập/phân quyền vì source hiện tại chưa triển khai cơ chế này.
- Chưa có kiểm thử hiệu năng và kiểm thử giao diện.

## 6. Minh chứng
Lưu ảnh chụp terminal sau khi chạy pytest vào thư mục `docs/screenshots/`. Chỉ đưa ảnh kết quả chạy thật, không dùng ảnh minh họa hoặc kết quả dự kiến.

## 7. Kiểm thử tự động bằng GitHub Actions (CI)

Workflow được cấu hình tại `.github/workflows/python-tests.yml`. Workflow tự động cài đặt Python 3.13 và các thư viện trong `requirements.txt`, sau đó chạy toàn bộ Pytest khi có push hoặc pull request vào nhánh `main`/`master`; có thể chạy thủ công bằng `workflow_dispatch`.

**Trạng thái CI:** Chưa xác nhận. Chỉ cập nhật thành PASS sau khi workflow thực sự chạy thành công trên GitHub Actions.

**Trang theo dõi:** `https://github.com/HaiVLU/cdtn1-NguyenHoTrungHai-L8/actions`
