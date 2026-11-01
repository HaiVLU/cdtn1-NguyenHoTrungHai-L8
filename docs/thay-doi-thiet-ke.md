Nhật ký ghi nhận phản hồi BT1 từ giảng viên cùng các quyết định điều chỉnh thiết kế kèm lý do kỹ thuật:
- Sơ đồ Use Case, kiến trúc và ERD chưa có chú thích ký hiệu; ảnh chụp nền đen nên chữ rất khó đọc. (Đã có chú thích ký hiệu; đã điều chỉnh để xem ảnh rõ ràng hơn
- Mô hình dữ liệu chưa tính được NPS: SURVEY_RESPONSE chỉ có score 1–5, thiếu điểm giới thiệu 0–10, trong khi wireframe và FR1–FR6 đều hiển thị NPS. Bảng mô tả SURVEY_RESPONSE còn thiếu cột date_id. (Đã bổ sung đầy đủ dữ liệu còn thiếu)
- Trang bìa chưa có link GitHub và track; phụ lục AI thiếu họ tên, MSSV, ngày trong dòng cam kết.(Đã bổ sung đầy đủ)
- Repo chưa có file gốc wireframe; commit chủ yếu "Add files via upload".(Đã điều chỉnh)

## THAY ĐỔI THIẾT KẾ BÀI TẬP 2:
## Thay đổi 1: Bổ sung xóa mềm cho khảo sát

- Thay đổi gì: Bổ sung trường is_deleted vào bảng SURVEY_RESPONSE và chuyển chức năng DELETE sang xóa mềm.
- Vì sao: Bảo toàn dữ liệu lịch sử khảo sát, phù hợp với W6 của BT1.
- Ảnh hưởng: src/models.py, src/repositories/survey_repository.py, src/services/survey_service.py, src/routes/report_routes.py và migration.

## Thay đổi 2: Bổ sung CRUD ServiceCenter

- Thay đổi gì: Bổ sung API tạo, đọc, cập nhật và xóa danh mục trung tâm bảo hành.
- Vì sao: Đáp ứng yêu cầu BT2 về tối thiểu hai thực thể có đủ CRUD.
- Ảnh hưởng: src/repositories/service_center_repository.py, src/services/service_center_service.py, src/routes/service_center_routes.py, src/__init__.py và API Contract.
