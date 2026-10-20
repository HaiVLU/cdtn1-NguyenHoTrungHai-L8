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
│   ├── 01-get-surveys.jpg
│   ├── 02-get-health.jpg
│   ├── ai-disclosure.md
│   ├── api-contract.md
│   ├── architecture.drawio
│   ├── erd.drawio
│   ├── srs.md
│   ├── thay-doi-thiet-ke.md
│   ├── usecase.drawio
│   ├── wireframe.drawio
│   └── wireframe.png
├── migrations/
├── src/
├── .env.example
├── .gitignore
├── package-lock.json
├── package.json
├── README.md
├── requirements.txt
├── run.py
└── seed.py

### Mô tả các tài liệu

- `docs/srs.md`: Đặc tả yêu cầu phần mềm (SRS), bao gồm yêu cầu chức năng, User Story, yêu cầu phi chức năng, quy tắc nghiệp vụ và bảng truy vết.
- `docs/usecase.drawio`: Sơ đồ Use Case của hệ thống.
- `docs/architecture.drawio`: Sơ đồ kiến trúc hệ thống.
- `docs/erd.drawio`: Sơ đồ mô hình dữ liệu ERD.
- `docs/wireframe.png`: Wireframe các màn hình của hệ thống.
- `docs/api-contract.md`: Đặc tả API dự kiến cho Track SE.
- `docs/ai-disclosure.md`: Bảng khai báo việc sử dụng công cụ AI.


## 3. Yêu cầu môi trường

### 3.1. Công nghệ sử dụng

- **Ngôn ngữ:** Python.
- **Framework:** Flask.
- **ORM:** Flask-SQLAlchemy.
- **Migration:** Flask-Migrate.
- **Cấu hình môi trường:** python-dotenv.
- **Cơ sở dữ liệu:** PostgreSQL.
- **Công cụ kiểm thử API:** Postman hoặc curl.
- **Quản lý mã nguồn:** Git và GitHub.

### 3.2. Yêu cầu cài đặt

Máy tính cần cài đặt:

- Python phiên bản tương thích với các thư viện của dự án.
- PostgreSQL và một cơ sở dữ liệu cục bộ dành cho ứng dụng.
- Git.
- Visual Studio Code hoặc IDE tương đương.
- Postman hoặc curl để kiểm thử các API.

### 3.3. Cài đặt và chạy dự án

**Bước 1: Tạo môi trường ảo**

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo trên Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**Bước 2: Cài đặt thư viện**

```bash
pip install -r requirements.txt
```

**Bước 3: Cấu hình biến môi trường**

Tạo file `.env` tại thư mục gốc dự án dựa trên `.env.example`. Cập nhật `SECRET_KEY` và `DATABASE_URL` theo cấu hình PostgreSQL trên máy cá nhân.

Không đưa file `.env` chứa thông tin bí mật lên GitHub.

**Bước 4: Khởi tạo hoặc cập nhật cấu trúc cơ sở dữ liệu**

Nếu dự án đã có migration được tạo và kiểm tra theo DDL của BT1, chạy:

```bash
flask --app run.py db upgrade
```

Nếu chưa khởi tạo migration, cần tạo và kiểm tra migration trước khi chạy lệnh cập nhật cơ sở dữ liệu.

**Bước 5: Nạp dữ liệu mẫu**

Chạy script seed nếu `seed.py` đã được cấu hình để nạp dữ liệu mẫu:

```bash
python seed.py
```

**Bước 6: Khởi chạy ứng dụng**

```bash
python run.py
```

Sau khi ứng dụng khởi động thành công, kiểm tra endpoint:

- `GET /health`: kiểm tra trạng thái hoạt động của API.
- `GET /api/surveys`: lấy danh sách khảo sát.

Địa chỉ chạy cục bộ mặc định:

```text
http://127.0.0.1:5000
```

Lưu ý: đường dẫn gốc `/` có thể trả về `404 Not Found` nếu chưa khai báo route trang chủ. Điều này không đồng nghĩa các API đã khai báo bị lỗi.

---

## 4. Trạng thái tiến độ hiện tại

### Các hạng mục đã triển khai

- Đã xây dựng bộ khung ứng dụng Flask cho bài tập BT2, Track SE.
- Đã cấu hình kết nối cơ sở dữ liệu thông qua biến môi trường `DATABASE_URL`.
- Đã tích hợp Flask-SQLAlchemy và Flask-Migrate trong ứng dụng.
- Đã tổ chức mã nguồn theo các lớp `routes`, `services` và `repositories`.
- Đã khai báo Blueprint cho module khảo sát tại `/api/surveys`.
- Đã xây dựng các endpoint khảo sát gồm:
  - `GET /api/surveys`: lấy danh sách khảo sát.
  - `GET /api/surveys/<response_id>`: lấy khảo sát theo ID.
  - `POST /api/surveys`: tạo khảo sát mới.
  - `PUT /api/surveys/<response_id>`: cập nhật khảo sát.
  - `DELETE /api/surveys/<response_id>`: xóa khảo sát.
- Đã khai báo endpoint `GET /health` để kiểm tra trạng thái hoạt động của ứng dụng.
- Đã chuẩn bị cấu hình môi trường qua `.env` và `.env.example`, cùng quy tắc loại trừ file không cần thiết qua `.gitignore`.
