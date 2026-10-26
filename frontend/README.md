# Frontend React — Smart CRM L8 CSAT/NPS

## Cài đặt
1. Mở terminal tại thư mục `frontend`.
2. Chạy `npm install`.
3. Sao chép `.env.example` thành `.env` và chỉnh `VITE_API_BASE_URL` nếu backend dùng cổng khác.
4. Chạy `npm run dev`.

## API
Frontend gọi các endpoint báo cáo được định nghĩa trong `docs/api-contract.md`:
- `GET /api/v1/reports/csat-nps/summary`
- `GET /api/v1/reports/csat-nps/trend`
- `GET /api/v1/reports/csat-nps/centers`
- `GET /api/v1/reports/csat-nps/technicians`

Backend ZIP hiện tại chưa triển khai các endpoint báo cáo này. Trang chi tiết tạm gọi endpoint hiện có `GET /api/surveys/:response_id`, endpoint này chỉ trả một phần trường dữ liệu. Xem ghi chú trong trang chi tiết trước khi coi là hoàn chỉnh.

## Demo
Trang kỹ thuật viên có checkbox để hiển thị tối đa hai bản ghi demo. Chúng được gắn nhãn `DEMO` và không được trộn tự động vào dữ liệu thật hoặc dùng trong tổng hợp báo cáo.
