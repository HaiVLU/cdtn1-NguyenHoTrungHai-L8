# Smart CRM – Mekong Mobile (BT2)

## 1. Giới thiệu

**Học phần:** Chuyên đề tốt nghiệp 2  
**Đề tài:** Smart CRM – Mekong Mobile  
**Luồng nghiệp vụ:** L8 – Khảo sát hài lòng CSAT/NPS sau khi phiếu bảo hành được đóng  
**Track:** SE  
**Sinh viên:** Nguyễn Hồ Trung Hải  
**MSSV:** 2374802010125

Hệ thống Smart CRM – Mekong Mobile được xây dựng nhằm hỗ trợ quản lý và theo dõi mức độ hài lòng của khách hàng sau khi sử dụng dịch vụ bảo hành.

Hệ thống sử dụng React cho giao diện, Flask cho Backend và PostgreSQL để lưu trữ dữ liệu. Backend cung cấp REST API phục vụ quản lý khảo sát, quản lý trung tâm dịch vụ và tổng hợp báo cáo CSAT/NPS.

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
│   ├── wireframe.png
│   └── test-results.jpg
├── migrations/
│   └── versions/
├── src/
│   ├── models.py
│   ├── extensions.py
│   ├── routes/
│   │   ├── survey_routes.py
│   │   ├── service_center_routes.py
│   │   └── report_routes.py
│   ├── services/
│   └── repositories/
├── tests/
│   └── test_survey_validation.py
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   └── pages/
│   ├── package.json
│   └── package-lock.json
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
├── seed.py
└── README.md
```

### Mô tả các thành phần

- `src/models.py`: Định nghĩa các model dữ liệu.
- `src/extensions.py`: Khởi tạo và quản lý các extension của ứng dụng.
- `src/routes/`: Tiếp nhận và xử lý các yêu cầu HTTP.
- `src/services/`: Xử lý nghiệp vụ và kiểm tra dữ liệu.
- `src/repositories/`: Thực hiện truy vấn dữ liệu.
- `migrations/`: Quản lý thay đổi cấu trúc cơ sở dữ liệu.
- `seed.py`: Nạp dữ liệu mẫu vào database.
- `tests/`: Chứa các bài kiểm thử Backend.
- `frontend/src/pages/`: Các màn hình giao diện.
- `frontend/src/api/`: Các hàm gọi REST API.
- `docs/`: Tài liệu phân tích, thiết kế và minh chứng.

## 3. Hướng dẫn chạy lại hệ thống

### 3.1. Yêu cầu môi trường

Máy tính cần cài đặt:

- Python tương thích với các thư viện trong `requirements.txt`.
- Node.js và npm.
- PostgreSQL.
- Git.
- Visual Studio Code hoặc IDE tương đương.
- Postman hoặc curl để kiểm thử API.
- Trình duyệt web.

Database sử dụng:

```text
l8_csat_nps
```

### 3.2. Chuẩn bị database PostgreSQL

Mở pgAdmin hoặc PostgreSQL và tạo database:

```sql
CREATE DATABASE l8_csat_nps;
```

Nếu database đã tồn tại thì không cần tạo lại.

### 3.3. Cài đặt và khởi động Backend

Mở PowerShell tại thư mục gốc repository.

**Bước 1 – Tạo môi trường Python ảo**

```powershell
python -m venv .venv
```

**Bước 2 – Kích hoạt môi trường**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Bước 3 – Cài đặt thư viện**

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Bước 4 – Tạo file cấu hình môi trường nếu chưa có**

```powershell
Copy-Item .env.example .env
```

Nếu file `.env` đã tồn tại, không ghi đè. Kiểm tra và cập nhật cấu hình hiện có.

**Bước 5 – Cấu hình kết nối PostgreSQL trong `.env`**

```env
SECRET_KEY=your-local-secret-key
DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@localhost:5432/l8_csat_nps
```

Thay `USERNAME` và `PASSWORD` bằng thông tin PostgreSQL thực tế trên máy.

**Bước 6 – Áp dụng migration**

```powershell
flask --app run.py db upgrade
```

Lệnh này tạo và cập nhật cấu trúc các bảng theo những migration có sẵn trong dự án.

**Bước 7 – Nạp dữ liệu mẫu**

```powershell
python seed.py
```

Chương trình kiểm tra dữ liệu trung tâm dịch vụ trước khi nạp. Nếu đã có dữ liệu mẫu, chương trình sẽ không nạp trùng.

**Bước 8 – Khởi động Backend**

```powershell
python run.py
```

Backend mặc định chạy tại:

```text
http://127.0.0.1:5000
```

**Bước 9 – Kiểm tra Backend**

Mở một cửa sổ PowerShell khác và chạy:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/health
```

Kết quả mong đợi:

```json
{
  "status": "ok",
  "message": "L8 API is running"
}
```

Các endpoint kiểm tra:

- `GET /health`: Kiểm tra trạng thái hoạt động của API.
- `GET /api/surveys`: Lấy danh sách khảo sát.

### 3.4. Cài đặt và khởi động Frontend

Mở một cửa sổ PowerShell mới.

**Bước 1 – Di chuyển vào thư mục Frontend**

```powershell
cd frontend
```

**Bước 2 – Tạo file `.env` nếu chưa có**

Tạo file `.env` trong thư mục `frontend` và cấu hình:

```env
VITE_API_BASE_URL=http://127.0.0.1:5000
```

Nếu đã có file `.env`, kiểm tra và cập nhật giá trị phù hợp, không ghi đè cấu hình hiện tại.

**Bước 3 – Cài đặt thư viện**

```powershell
npm ci
```

**Bước 4 – Khởi động Frontend**

```powershell
npm run dev
```

Truy cập địa chỉ do Vite hiển thị, thông thường:

```text
http://localhost:5173
```

### 3.5. Kiểm tra các màn hình

| Đường dẫn | Chức năng |
|---|---|
| `/` | Tổng quan CSAT/NPS |
| `/technicians` | Báo cáo kỹ thuật viên |
| `/surveys/:id` | Chi tiết khảo sát |

### 3.6. Kiểm thử Backend

Tại thư mục gốc repository, kích hoạt môi trường `.venv` và chạy:

```powershell
python -m pytest -o pythonpath=. -v
```

Các test hiện tại tập trung kiểm tra:

- Dữ liệu khảo sát hợp lệ.
- Giá trị biên CSAT/NPS.
- Thiếu trường bắt buộc.
- Điểm CSAT vượt giới hạn.
- Kiểu dữ liệu không hợp lệ.

### 3.7. Kiểm tra build Frontend

Tại thư mục `frontend`, chạy:

```powershell
npm run build
```

Nếu build thành công, Vite tạo thư mục `dist/` chứa sản phẩm build.

## 4. Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| Frontend | React, Vite |
| Backend | Python, Flask |
| Database | PostgreSQL |
| ORM | Flask-SQLAlchemy |
| Migration | Flask-Migrate |
| API | REST API |
| Kiểm thử | pytest |
| Quản lý mã nguồn | Git, GitHub |

## 5. Các module chức năng

- **Survey Module:** Quản lý danh sách, chi tiết, tạo, cập nhật và xóa khảo sát.
- **Service Center Module:** Quản lý thông tin trung tâm dịch vụ.
- **Report Module:** Tổng hợp và thống kê dữ liệu CSAT/NPS theo thời gian, trung tâm và kỹ thuật viên.
- **Frontend Module:** Hiển thị tổng quan, báo cáo kỹ thuật viên và chi tiết khảo sát.

## 6. Trạng thái tiến độ hiện tại

### 6.1. Các hạng mục đã triển khai

- Đã xây dựng bộ khung ứng dụng Flask cho bài tập BT2, Track SE.
- Đã cấu hình kết nối cơ sở dữ liệu thông qua biến môi trường `DATABASE_URL`.
- Đã tích hợp Flask-SQLAlchemy và Flask-Migrate trong ứng dụng.
- Đã tổ chức mã nguồn theo các lớp `routes`, `services` và `repositories`.
- Đã khai báo Blueprint cho module khảo sát tại `/api/surveys`.
- Đã xây dựng các API quản lý khảo sát.
- Đã xây dựng API quản lý trung tâm dịch vụ.
- Đã triển khai API báo cáo CSAT/NPS.
- Đã xây dựng giao diện Frontend bằng React.
- Đã khai báo endpoint `GET /health` để kiểm tra trạng thái hoạt động của ứng dụng.
- Đã chuẩn bị cấu hình môi trường qua `.env` và `.env.example`.
- Đã cấu hình `.gitignore` để loại trừ các file và thư mục không cần thiết.

### 6.2. Kiểm thử và minh chứng

- Đã xây dựng các test kiểm tra dữ liệu khảo sát bằng pytest.
- Đã chuẩn bị ảnh minh chứng kiểm thử API trong thư mục `docs/`.
- Đã kiểm tra API sức khỏe hệ thống và API danh sách khảo sát.
- Đã chuẩn bị tài liệu thiết kế, API Contract và tài liệu khai báo sử dụng AI.

### 6.3. Các giới hạn hiện tại

- Trang chi tiết khảo sát chưa nhận đầy đủ thông tin trung tâm, kỹ thuật viên và khách hàng từ API.
- Bản ghi DEMO trên trang kỹ thuật viên là dữ liệu minh họa, không phải dữ liệu thật từ PostgreSQL.
- Kiểm thử hiện tại tập trung vào hàm kiểm tra dữ liệu khảo sát, chưa đại diện cho toàn bộ kiểm thử tích hợp và giao diện.
- Chỉ số NPS trong API hiện tại đang được trả về dưới dạng điểm trung bình trên thang 0–10, chưa phải chỉ số NPS tổng hợp theo tỷ lệ Promoters trừ Detractors.

## 7. Bảo mật và cấu hình

- Không commit file `.env` lên GitHub.
- Sử dụng `.env.example` để cung cấp cấu hình mẫu.
- Không đưa mật khẩu database hoặc thông tin bí mật vào source code.
- Không commit thư mục môi trường ảo `.venv/`, `venv/`.
- Không commit thư mục `node_modules/`.
- Không commit các sản phẩm build không cần thiết.
- Không công khai thông tin xác thực hoặc khóa bí mật trong repository.

---

**Dự án:** Smart CRM – Mekong Mobile  
**Học phần:** Chuyên đề tốt nghiệp 2  
**Track:** Software Engineering (SE)
