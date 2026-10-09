# I. SRS – HỆ THỐNG BÁO CÁO CSAT/NPS

## 1. Giới thiệu

### 1.1. Mục đích

Hệ thống hỗ trợ Marketing, Quản lý trung tâm và Ban giám đốc theo dõi, phân tích kết quả khảo sát CSAT/NPS sau khi phiếu bảo hành được đóng.

### 1.2. Phạm vi

Các chức năng của hệ thống bao gồm:

* Xem CSAT/NPS theo thời gian.
* Xem CSAT/NPS theo trung tâm.
* Quản lý trung tâm xem dữ liệu của trung tâm mình.
* Xem CSAT/NPS theo kỹ thuật viên.
* Ban giám đốc xem báo cáo tổng hợp.
* Ban giám đốc xem báo cáo theo trung tâm và thời gian.
* Kiểm soát phạm vi dữ liệu theo quyền được phân công.

### 1.3. WON'T – Ngoài phạm vi

| Mã | Nội dung                                                                          |
| -- | --------------------------------------------------------------------------------- |
| W1 | Không quản lý toàn bộ quy trình bảo hành.                                         |
| W2 | Không quản lý hoặc chỉnh sửa thông tin khách hàng ngoài phạm vi cần cho khảo sát. |
| W3 | Không xử lý sửa chữa hoặc phân công kỹ thuật viên.                                |
| W4 | Không xây dựng mô hình dự đoán mức độ hài lòng bằng AI/ML.                        |
| W5 | Không triển khai hệ thống gửi SMS/email marketing độc lập.                        |
| W6 | Không thực hiện xóa vật lý dữ liệu lịch sử khảo sát.                              |

### 1.4. Bảng thuật ngữ

| Thuật ngữ         | Ý nghĩa                                                         |
| ----------------- | --------------------------------------------------------------- |
| CSAT              | Chỉ số đo mức độ hài lòng của khách hàng.                       |
| NPS               | Chỉ số đo khả năng khách hàng giới thiệu sản phẩm hoặc dịch vụ. |
| Phiếu bảo hành    | Hồ sơ bảo hành của khách hàng.                                  |
| Khảo sát          | Phản hồi của khách hàng sau khi phiếu bảo hành được đóng.       |
| Trung tâm         | Trung tâm bảo hành.                                             |
| Kỹ thuật viên     | Nhân viên thực hiện bảo hành.                                   |
| Marketing         | Người phân tích CSAT/NPS.                                       |
| Quản lý trung tâm | Người quản lý dữ liệu của trung tâm mình phụ trách.             |
| Ban giám đốc      | Người xem báo cáo tổng hợp trên toàn công ty.                   |

## 2. Actors & Roles

| Actor             | Quyền / trách nhiệm                                                       |
| ----------------- | ------------------------------------------------------------------------- |
| Marketing         | Xem và phân tích CSAT/NPS theo thời gian và trung tâm.                    |
| Quản lý trung tâm | Xem CSAT/NPS của trung tâm mình và theo kỹ thuật viên thuộc trung tâm.    |
| Ban giám đốc      | Xem báo cáo tổng hợp toàn công ty và phân tích theo trung tâm, thời gian. |

## 3. Yêu cầu chức năng

### 3.1. Functional Requirements

| ID  | Functional Requirement                                               | US  | MoSCoW |
| --- | -------------------------------------------------------------------- | --- | ------ |
| FR1 | Xem CSAT/NPS theo khoảng thời gian.                                  | US1 | MUST   |
| FR2 | Xem và so sánh CSAT/NPS theo trung tâm.                              | US2 | MUST   |
| FR3 | Quản lý trung tâm xem CSAT/NPS của trung tâm mình.                   | US3 | MUST   |
| FR4 | Quản lý xem CSAT/NPS theo kỹ thuật viên.                             | US4 | MUST   |
| FR5 | Ban giám đốc xem báo cáo CSAT/NPS tổng hợp.                          | US5 | MUST   |
| FR6 | Ban giám đốc xem CSAT/NPS theo trung tâm và thời gian.               | US6 | SHOULD |
| FR7 | Kiểm soát để Quản lý trung tâm chỉ xem dữ liệu thuộc trung tâm mình. | US7 | MUST   |

### 3.2. User Stories

| ID  | User Story                                                                                                                             | MoSCoW |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| US1 | Là Marketing, tôi muốn xem chỉ số CSAT/NPS theo thời gian để theo dõi xu hướng hài lòng của khách hàng.                                | MUST   |
| US2 | Là Marketing, tôi muốn xem kết quả CSAT/NPS theo từng trung tâm để so sánh mức độ hài lòng giữa các trung tâm.                         | MUST   |
| US3 | Là Quản lý trung tâm, tôi muốn xem chỉ số CSAT/NPS của trung tâm mình để đánh giá chất lượng dịch vụ.                                  | MUST   |
| US4 | Là Quản lý trung tâm, tôi muốn xem kết quả CSAT/NPS theo kỹ thuật viên để theo dõi chất lượng phục vụ của từng kỹ thuật viên.          | MUST   |
| US5 | Là Ban giám đốc, tôi muốn xem báo cáo CSAT/NPS tổng hợp để theo dõi chất lượng dịch vụ trên toàn công ty.                              | MUST   |
| US6 | Là Ban giám đốc, tôi muốn xem kết quả CSAT/NPS theo trung tâm và thời gian để đánh giá xu hướng và hiệu quả dịch vụ.                   | SHOULD |
| US7 | Là Quản lý trung tâm, tôi muốn chỉ xem được dữ liệu thuộc phạm vi trung tâm mình phụ trách để đảm bảo dữ liệu được phân quyền phù hợp. | MUST   |

## 4. Non-functional Requirements

| ID   | Non-functional Requirement                                                           | Ngưỡng đo được                                                                             |
| ---- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| NFR1 | **Hiệu năng:** Hệ thống hiển thị kết quả CSAT/NPS sau khi người dùng chọn bộ lọc.    | Thời gian hiển thị không quá 2 giây với tối đa 10.000 bản ghi khảo sát.                    |
| NFR2 | **Tính toàn vẹn dữ liệu:** Một phiếu bảo hành không tạo nhiều khảo sát hợp lệ.       | 100% phiếu bảo hành có tối đa 1 khảo sát hợp lệ.                                           |
| NFR3 | **Kiểm soát truy cập:** Quản lý trung tâm không được xem dữ liệu của trung tâm khác. | 100% yêu cầu của Quản lý trung tâm chỉ trả về dữ liệu thuộc trung tâm được phân quyền.     |
| NFR4 | **Bảo mật thông tin khách hàng:** Số điện thoại phải được che theo quy định.         | 100% số điện thoại hiển thị cho Quản lý trung tâm và Ban giám đốc được masking theo QT-15. |

## 5. Business Rules

| ID    | Business Rules                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------ |
| QT-10 | Chỉ gửi khảo sát cho phiếu bảo hành ở trạng thái **ĐÃ ĐÓNG** và mỗi phiếu chỉ được khảo sát một lần.               |
| QT-13 | Không xóa vật lý phiếu bảo hành, đơn hàng hoặc hồ sơ khách hàng; chỉ soft delete và giữ nguyên lịch sử.            |
| QT-14 | Quản lý trung tâm chỉ xem dữ liệu thuộc trung tâm mình phụ trách; Ban giám đốc được xem dữ liệu trên toàn công ty. |
| QT-15 | Số điện thoại khách hàng phải được hiển thị dưới dạng che theo quy định.                                           |

## 6. Traceability Matrix

| Functional Requirement | User Story | Use Case | MoSCoW |
| ---------------------- | ---------- | -------- | ------ |
| FR1                    | US1        | UC1      | MUST   |
| FR2                    | US2        | UC2      | MUST   |
| FR3                    | US3        | UC3      | MUST   |
| FR4                    | US4        | UC4      | MUST   |
| FR5                    | US5        | UC5      | MUST   |
| FR6                    | US6        | UC6      | SHOULD |
| FR7                    | US7        | UC7      | MUST   |

