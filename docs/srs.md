1. INTRODUCTION & SCOPE
1.1. Mục đích
Luồng L8 – Khảo sát hài lòng CSAT/NPS tập trung vào việc Marketing, Quản lý trung tâm và Ban giám đốc xem và phân tích kết quả khảo sát sau khi phiếu bảo hành được đóng.
Hệ thống hỗ trợ phân tích kết quả CSAT/NPS theo trung tâm, kỹ thuật viên và thời gian, đồng thời kiểm soát quyền truy cập và đảm bảo mỗi phiếu chỉ được khảo sát một lần.
1.2. Phạm vi hệ thống
Hệ thống hỗ trợ các chức năng sau:
Xem CSAT/NPS theo khoảng thời gian. 
Xem và so sánh CSAT/NPS theo trung tâm. 
Quản lý trung tâm xem kết quả của trung tâm mình. 
Quản lý trung tâm xem CSAT/NPS theo kỹ thuật viên thuộc trung tâm. 
Ban giám đốc xem báo cáo tổng hợp toàn công ty. 
Ban giám đốc xem CSAT/NPS theo trung tâm và thời gian. 
Kiểm soát quyền truy cập theo vai trò. 
Bảo toàn dữ liệu lịch sử liên quan đến khảo sát. 
Che số điện thoại khách hàng khi hiển thị cho các vai trò được quy định. 
1.3. WON'T – Ngoài phạm vi
Mã	Nội dung
W1	Không quản lý toàn bộ quy trình bảo hành.
W2	Không quản lý/chỉnh sửa thông tin khách hàng ngoài phạm vi cần cho khảo sát.
W3	Không xử lý sửa chữa hoặc phân công kỹ thuật viên.
W4	Không xây dựng mô hình dự đoán mức độ hài lòng bằng AI/ML.
W5	Không triển khai hệ thống gửi SMS/email marketing độc lập.
W6	Không thực hiện xóa vật lý dữ liệu lịch sử khảo sát.
1.4. Bảng thuật ngữ
Thuật ngữ	Định nghĩa
CSAT	Chỉ số đo mức độ hài lòng của khách hàng sau dịch vụ.
NPS	Chỉ số đo khả năng khách hàng giới thiệu dịch vụ cho người khác.
Phiếu bảo hành	Hồ sơ ghi nhận một trường hợp bảo hành của khách hàng.
Khảo sát	Phiếu khảo sát mức độ hài lòng được thực hiện sau khi phiếu bảo hành đóng.
Trung tâm	Đơn vị/cửa hàng/trung tâm tiếp nhận và xử lý bảo hành.
Kỹ thuật viên	Nhân viên kỹ thuật thực hiện dịch vụ bảo hành.
Marketing	Người theo dõi và phân tích chất lượng dịch vụ thông qua CSAT/NPS.
Quản lý trung tâm	Người quản lý dữ liệu và chất lượng dịch vụ tại trung tâm của mình.
Ban giám đốc	Người xem báo cáo tổng hợp ở phạm vi toàn công ty.

2. ACTORS & ROLES
Actor	Quyền / trách nhiệm
Marketing	Xem và phân tích CSAT/NPS theo thời gian và trung tâm.
Quản lý trung tâm	Xem CSAT/NPS của trung tâm mình và theo kỹ thuật viên thuộc trung tâm.
Ban giám đốc	Xem báo cáo tổng hợp toàn công ty và phân tích theo trung tâm/thời gian.
Quy tắc phân quyền
Quyền truy cập dữ liệu được áp dụng theo QT-14:
Quản lý trung tâm chỉ được xem dữ liệu thuộc trung tâm mình phụ trách. 
Ban giám đốc được xem dữ liệu trong phạm vi toàn công ty. 
Người dùng không được truy cập dữ liệu ngoài phạm vi quyền được cấp. 

3. FUNCTIONAL REQUIREMENTS & USER STORIES
3.1. Functional Requirements
ID	Functional Requirement	User Story	MoSCoW
FR1	Cho phép người dùng có quyền xem CSAT/NPS theo khoảng thời gian được chọn.	US1	MUST
FR2	Cho phép xem và so sánh CSAT/NPS theo trung tâm.	US2	MUST
FR3	Cho phép Quản lý trung tâm xem CSAT/NPS của trung tâm mình.	US3	MUST
FR4	Cho phép Quản lý trung tâm xem CSAT/NPS theo kỹ thuật viên thuộc trung tâm mình.	US4	MUST
FR5	Cho phép Ban giám đốc xem báo cáo CSAT/NPS tổng hợp toàn công ty.	US5	MUST
FR6	Cho phép Ban giám đốc xem CSAT/NPS theo trung tâm và khoảng thời gian.	US6	SHOULD
FR7	Kiểm soát quyền để Quản lý trung tâm chỉ xem dữ liệu thuộc trung tâm mình.	US7	MUST
FR8	Cho phép số điện thoại khách hàng được hiển thị ở dạng che đối với vai trò được quy định.	US8	MUST

3.2. User Stories
US1 – Xem CSAT/NPS theo thời gian – MUST
Là Marketing, tôi muốn xem chỉ số CSAT/NPS theo thời gian để theo dõi xu hướng hài lòng của khách hàng.
US2 – Xem CSAT/NPS theo trung tâm – MUST
Là Marketing, tôi muốn xem kết quả CSAT/NPS theo từng trung tâm để so sánh mức độ hài lòng giữa các trung tâm.
US3 – Quản lý xem CSAT/NPS của trung tâm – MUST
Là Quản lý trung tâm, tôi muốn xem chỉ số CSAT/NPS của trung tâm mình để đánh giá chất lượng dịch vụ.
US4 – Xem CSAT/NPS theo kỹ thuật viên – MUST
Là Quản lý trung tâm, tôi muốn xem kết quả CSAT/NPS theo kỹ thuật viên để theo dõi chất lượng phục vụ của từng kỹ thuật viên.
US5 – Xem báo cáo tổng hợp – MUST
Là Ban giám đốc, tôi muốn xem báo cáo CSAT/NPS tổng hợp để theo dõi chất lượng dịch vụ trên toàn công ty.
US6 – Xem CSAT/NPS theo trung tâm và thời gian – SHOULD
Là Ban giám đốc, tôi muốn xem kết quả CSAT/NPS theo trung tâm và thời gian để đánh giá xu hướng và hiệu quả dịch vụ.
US7 – Kiểm soát phạm vi dữ liệu – MUST
Là Quản lý trung tâm, tôi muốn chỉ xem được dữ liệu thuộc phạm vi trung tâm mình phụ trách để đảm bảo dữ liệu được phân quyền phù hợp.
US8 – Che số điện thoại khách hàng – MUST
Là Quản lý trung tâm, tôi muốn xem thông tin số điện thoại khách hàng được che khi xem báo cáo để bảo vệ thông tin cá nhân của khách hàng.

3.3. Acceptance Criteria cho các Story MUST
US1 – Xem CSAT/NPS theo thời gian
AC1 – Thành công
Given: Marketing đã đăng nhập và có quyền xem báo cáo.
When: Marketing chọn một khoảng thời gian hợp lệ.
Then: Hệ thống hiển thị kết quả CSAT/NPS tương ứng với khoảng thời gian đã chọn.
AC2 – Ngoại lệ
Given: Marketing đã đăng nhập.
When: Marketing nhập khoảng thời gian không hợp lệ hoặc ngày bắt đầu lớn hơn ngày kết thúc.
Then: Hệ thống thông báo lỗi và yêu cầu Marketing chọn lại khoảng thời gian.

US2 – Xem CSAT/NPS theo trung tâm
AC1 – Thành công
Given: Marketing đã đăng nhập và có quyền xem báo cáo.
When: Marketing chọn một trung tâm.
Then: Hệ thống hiển thị kết quả CSAT/NPS của trung tâm được chọn.
AC2 – Ngoại lệ
Given: Marketing đã chọn một trung tâm.
When: Trung tâm không có dữ liệu khảo sát.
Then: Hệ thống hiển thị thông báo "Không có dữ liệu khảo sát."

US3 – Quản lý xem CSAT/NPS của trung tâm
AC1 – Thành công
Given: Quản lý trung tâm đã đăng nhập và được phân quyền cho một trung tâm.
When: Quản lý mở báo cáo CSAT/NPS.
Then: Hệ thống hiển thị kết quả CSAT/NPS của trung tâm được phân quyền.
AC2 – Ngoại lệ
Given: Quản lý đang được phân quyền cho Trung tâm A.
When: Quản lý cố truy cập dữ liệu của Trung tâm B.
Then: Hệ thống từ chối truy cập và không hiển thị dữ liệu ngoài phạm vi.

US4 – Xem CSAT/NPS theo kỹ thuật viên
AC1 – Thành công
Given: Quản lý trung tâm đã đăng nhập và được gắn với một trung tâm.
When: Quản lý chọn chức năng phân tích theo kỹ thuật viên.
Then: Hệ thống hiển thị CSAT/NPS theo các kỹ thuật viên thuộc trung tâm được phân quyền.
AC2 – Ngoại lệ
Given: Quản lý đang được phân quyền cho Trung tâm A.
When: Quản lý cố truy cập dữ liệu của Trung tâm B.
Then: Hệ thống từ chối truy cập và không hiển thị dữ liệu ngoài phạm vi.

US5 – Xem báo cáo tổng hợp
AC1 – Thành công
Given: Ban giám đốc đã đăng nhập và có quyền xem dữ liệu toàn công ty.
When: Ban giám đốc mở báo cáo CSAT/NPS tổng hợp.
Then: Hệ thống hiển thị kết quả CSAT/NPS tổng hợp trên toàn công ty.

US7 – Kiểm soát phạm vi dữ liệu
AC1 – Thành công
Given: Quản lý trung tâm được phân quyền cho Trung tâm A.
When: Quản lý yêu cầu xem báo cáo.
Then: Hệ thống chỉ trả về dữ liệu thuộc Trung tâm A.
AC2 – Ngoại lệ
Given: Quản lý được phân quyền cho Trung tâm A.
When: Quản lý yêu cầu dữ liệu Trung tâm B.
Then: Hệ thống từ chối truy cập.

US8 – Che số điện thoại khách hàng
AC1
Given: Người dùng có vai trò Quản lý trung tâm.
When: Người dùng xem báo cáo có thông tin khách hàng.
Then: Số điện thoại khách hàng phải được hiển thị ở dạng che.
AC2
Given: Người dùng có vai trò Ban giám đốc.
When: Người dùng xem báo cáo có thông tin khách hàng.
Then: Số điện thoại khách hàng phải được hiển thị ở dạng che.

4. NON-FUNCTIONAL REQUIREMENTS
ID	Non-functional Requirement	Ngưỡng đo được
NFR1	Hiệu năng: Hệ thống hiển thị kết quả CSAT/NPS sau khi người dùng chọn bộ lọc.	≤ 2 giây với tối đa 10.000 bản ghi khảo sát.
NFR2	Tính toàn vẹn dữ liệu: Một phiếu bảo hành không tạo nhiều khảo sát hợp lệ.	100% phiếu bảo hành có tối đa 1 khảo sát hợp lệ.
NFR3	Kiểm soát truy cập: Quản lý trung tâm không được xem dữ liệu của trung tâm khác.	100% yêu cầu của Quản lý chỉ trả dữ liệu thuộc trung tâm được phân quyền.
NFR4	Bảo mật thông tin khách hàng: Số điện thoại phải được che theo quy định.	100% số điện thoại hiển thị cho Quản lý và Ban giám đốc được masking theo QT-15.

5. BUSINESS RULES
Mã	Quy tắc nghiệp vụ	Áp dụng cho L8
QT-10	Chỉ gửi khảo sát cho phiếu ở trạng thái ĐÃ ĐÓNG; mỗi phiếu chỉ khảo sát một lần.	Đảm bảo dữ liệu khảo sát hợp lệ và không khảo sát trùng phiếu.
QT-13	Không xóa vật lý phiếu bảo hành, đơn hàng hoặc hồ sơ khách hàng; chỉ soft delete và giữ nguyên lịch sử.	Đảm bảo dữ liệu lịch sử liên quan đến khảo sát vẫn có thể truy vết.
QT-14	Nhân viên chỉ xem dữ liệu của trung tâm/cửa hàng mình; Quản lý xem phạm vi phụ trách; Ban giám đốc xem toàn công ty.	Kiểm soát phạm vi dữ liệu khi xem CSAT/NPS.
QT-15	Số điện thoại khách hàng hiển thị dạng che đối với vai trò từ Quản lý và Ban giám đốc.	Bảo vệ thông tin cá nhân khi xem báo cáo.
QT-10 là quy tắc trực tiếp nhất với L8. QT-14 và QT-15 tạo cơ sở cho các yêu cầu về phân quyền và bảo vệ dữ liệu. QT-13 bảo đảm dữ liệu lịch sử liên quan vẫn có thể được truy vết. 

6. TRACEABILITY MATRIX
FR	User Story	Use Case	MoSCoW
FR1	US1 – Xem CSAT/NPS theo thời gian	UC1 – Xem CSAT/NPS theo thời gian	MUST
FR2	US2 – Xem CSAT/NPS theo trung tâm	UC2 – Xem CSAT/NPS theo trung tâm	MUST
FR3	US3 – Xem CSAT/NPS của trung tâm	UC3 – Xem CSAT/NPS của trung tâm	MUST
FR4	US4 – Xem CSAT/NPS theo kỹ thuật viên	UC4 – Xem CSAT/NPS theo kỹ thuật viên	MUST
FR5	US5 – Xem báo cáo CSAT/NPS tổng hợp	UC5 – Xem báo cáo CSAT/NPS tổng hợp	MUST
FR6	US6 – Xem CSAT/NPS theo trung tâm và thời gian	UC6 – Xem CSAT/NPS theo trung tâm và thời gian	SHOULD
FR7	US7 – Kiểm soát phạm vi dữ liệu	UC7 – Kiểm soát phạm vi dữ liệu	MUST
FR8	US8 – Che số điện thoại khách hàng	NFR4 / QT-15	MUST
Kiểm tra tính truy vết
Không có User Story nào không có FR. 
Không có FR nào không có User Story. 
FR1–FR7 có Use Case tương ứng. 
FR8 được truy vết đến yêu cầu bảo mật NFR4/QT-15. 
MoSCoW được xác định cho toàn bộ 8 User Story. 
