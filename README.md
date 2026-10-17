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

