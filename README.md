# Smart CRM – Mekong Mobile (BT1)

## 1. Giới thiệu

**Học phần:** Chuyên đề tốt nghiệp 1 – Bài tập 1: Phân tích và Thiết kế  
**Đề tài:** Smart CRM – Mekong Mobile  
**Luồng nghiệp vụ:** L8: Khảo sát hài lòng CSAT/NPS sau khi phiếu bảo hành được đóng  
**Track:** SE  
**Sinh viên:** Nguyễn Hồ Trung Hải  
**MSSV:** 2374802010125

Repository này lưu trữ các tài liệu phân tích và thiết kế của BT1. Phạm vi hiện tại tập trung vào tài liệu đặc tả, sơ đồ thiết kế và mô hình dữ liệu; chưa triển khai mã nguồn ứng dụng.

Hệ thống hỗ trợ Marketing, Quản lý trung tâm và Ban giám đốc theo dõi, phân tích kết quả khảo sát CSAT/NPS. Quản lý trung tâm chỉ được xem dữ liệu thuộc trung tâm được phân quyền. Số điện thoại khách hàng phải được che theo quy định.

## 2. Cấu trúc repository

```text
.
├── docs/
│   ├── ai-disclosure.md
│   ├── api-contract.md
│   ├── architecture.drawio
│   ├── erd.drawio
│   ├── srs.md
│   ├── usecase.drawio
│   └── wireframe.png
├── .env.example
├── .gitignore
└── README.md
```

### Mô tả các tài liệu

- `docs/srs.md`: Đặc tả yêu cầu phần mềm (SRS), bao gồm yêu cầu chức năng, User Story, yêu cầu phi chức năng, quy tắc nghiệp vụ và bảng truy vết.
- `docs/usecase.drawio`: Sơ đồ Use Case của hệ thống.
- `docs/architecture.drawio`: Sơ đồ kiến trúc hệ thống.
- `docs/erd.drawio`: Sơ đồ mô hình dữ liệu ERD.
- `docs/wireframe.png`: Wireframe các màn hình của hệ thống.
- `docs/api-contract.md`: Đặc tả API dự kiến cho Track SE.
- `docs/ai-disclosure.md`: Bảng khai báo việc sử dụng công cụ AI.

## 3. Hướng dẫn chạy lại hệ thống

### 3.1. Yêu cầu môi trường

- Python đã được cài đặt.
- Node.js và npm đã được cài đặt.
- PostgreSQL đang hoạt động.
- Đã có database `l8_csat_nps` và dữ liệu mẫu cần thiết.
- Backend Flask và frontend React/Vite nằm trong repository.
- File `.env.example` chứa mẫu cấu hình kết nối database; không đưa mật khẩu thật vào GitHub.

### 3.2. Khởi động PostgreSQL

**Bước 1:** Kiểm tra PostgreSQL có hoạt động và database `l8_csat_nps` đã tồn tại. Có thể kiểm tra bằng pgAdmin hoặc `psql`.

### 3.3. Khởi động Backend Flask

Thực hiện các lệnh sau trong PowerShell tại thư mục gốc repository.

**Bước 1 — Tạo môi trường Python ảo:**

```powershell
python -m venv venv
```

**Bước 2 — Kích hoạt môi trường ảo:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Bước 3 — Cài đặt thư viện backend:**

```powershell
pip install -r requirements.txt
```

**Bước 4 — Tạo file cấu hình môi trường từ file mẫu nếu chưa có:**

```powershell
Copy-Item .env.example .env
```

Nếu file `.env` đã tồn tại, không ghi đè file đó; hãy kiểm tra và cập nhật cấu hình hiện có.

**Bước 5 — Cập nhật `DATABASE_URL` trong file `.env` để kết nối tới database `l8_csat_nps`:**

```dotenv
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@localhost:5432/l8_csat_nps
```

Thay `USERNAME` và `PASSWORD` bằng thông tin PostgreSQL trên máy.

**Bước 6 — Nếu dự án đã cấu hình Flask-Migrate và có thư mục migration, cập nhật cấu trúc database:**

```powershell
flask db upgrade
```

Chỉ chạy bước này khi migration đã được thiết lập trong dự án. Không tự tạo migration mới hoặc sửa dữ liệu database chỉ để chạy theo hướng dẫn.

**Bước 7 — Khởi động backend:**

```powershell
python run.py
```

Backend chạy tại `http://127.0.0.1:5000` nếu cấu hình hiện tại sử dụng cổng mặc định.

**Bước 8 — Kiểm tra API health:**

```powershell
Invoke-RestMethod http://127.0.0.1:5000/health
```

Kết quả mong đợi là phản hồi JSON thể hiện API đang hoạt động.

### 3.4. Khởi động Frontend React/Vite

Mở **một cửa sổ PowerShell khác** tại thư mục chứa `package.json` của frontend.

**Bước 1 — Cài đặt các thư viện frontend:**

```powershell
npm install
```

**Bước 2 — Khởi động frontend ở chế độ phát triển:**

```powershell
npm run dev
```

Mở địa chỉ localhost được Vite hiển thị trong terminal để sử dụng giao diện.

### 3.5. Kiểm tra sau khi khởi động

- Backend Flask khởi động không có lỗi.
- API `/health` trả về phản hồi thành công.
- Frontend mở được trên trình duyệt.
- Frontend kết nối đúng địa chỉ backend.
- Các API báo cáo CSAT/NPS trả về dữ liệu.
- Dữ liệu ticket, khảo sát và trung tâm dịch vụ được hiển thị đúng với database hiện tại.

Lưu ý: Các lệnh trên giả định repository có `requirements.txt`, `run.py`, cấu hình Flask-Migrate và frontend có `package.json`. Nếu cấu trúc thực tế khác, cần điều chỉnh đường dẫn và lệnh tương ứng.

