Nhật ký ghi nhận phản hồi BT1 từ giảng viên cùng các quyết định điều chỉnh thiết kế kèm lý do kỹ thuật:
- Sơ đồ Use Case, kiến trúc và ERD chưa có chú thích ký hiệu; ảnh chụp nền đen nên chữ rất khó đọc. (Đã có chú thích ký hiệu; đã điều chỉnh để xem ảnh rõ ràng hơn
- Mô hình dữ liệu chưa tính được NPS: SURVEY_RESPONSE chỉ có score 1–5, thiếu điểm giới thiệu 0–10, trong khi wireframe và FR1–FR6 đều hiển thị NPS. Bảng mô tả SURVEY_RESPONSE còn thiếu cột date_id. (Đã bổ sung đầy đủ dữ liệu còn thiếu)
- Trang bìa chưa có link GitHub và track; phụ lục AI thiếu họ tên, MSSV, ngày trong dòng cam kết.(Đã bổ sung đầy đủ)
- Repo chưa có file gốc wireframe; commit chủ yếu "Add files via upload".(Đã điều chỉnh)

NHẬT KÝ THAY ĐỔI THIẾT KẾ VÀ KHẮC PHỤC PHẢN HỒI BT2
Sinh viên: Nguyễn Hồ Trung Hải
MSSV: 2374802010125
Dự án: Smart CRM – Khảo sát hài lòng CSAT/NPS
Công nghệ: Flask, PostgreSQL, React, Vite  

Tài liệu này ghi nhận các phản hồi của giảng viên sau BT2, những nội dung đã hoàn thiện, lý do điều chỉnh, phạm vi ảnh hưởng và cách kiểm chứng. Các minh chứng thực tế được lưu trong thư mục docs/ của repository và trong Test Plan/Test Report.
1. Tổng hợp phản hồi BT2 và kết quả khắc phục
STT	Nội dung giảng viên góp ý	Nội dung đã hoàn thiện	Cách kiểm chứng
1	Chưa có minh chứng đầy đủ cho ba trạng thái Loading, Empty, Error của S4.	Hoàn thiện cách hiển thị trạng thái đang tải dữ liệu, không có dữ liệu và lỗi khi tải dữ liệu trên giao diện. Trạng thái lỗi có thông báo và chức năng thử tải lại.	Chạy giao diện và kiểm tra lần lượt ba tình huống; đối chiếu ảnh chụp minh chứng S4 trong docs/ và phần kiểm thử tương ứng trong Test Report.
2	Phần kiểm thử còn ngắn, chưa thể hiện rõ quá trình thực hiện và kết quả.	Bổ sung Test Plan, Test Report, Bug Log; mô tả phạm vi, điều kiện, các bước thực hiện, kết quả mong đợi, kết quả thực tế và trạng thái từng test case.	Đối chiếu Test Plan với Test Report; kiểm tra các test case đã chạy và kết quả thực tế; đối chiếu Bug Log với lỗi và commit sửa lỗi (nếu có).
3	Repository chứa frontend/node_modules, làm tăng dung lượng và đưa thư viện cài đặt vào mã nguồn.	Bổ sung quy tắc loại trừ node_modules/ trong .gitignore; loại bỏ thư mục frontend/node_modules khỏi Git tracking. Các thư viện được cài lại bằng npm install từ package.json và lockfile.	Kiểm tra .gitignore, chạy git status và git ls-files để xác nhận node_modules không còn được Git theo dõi.
4	Hệ thống chưa có chức năng đăng nhập.	Bổ sung trang đăng nhập Admin, kiểm tra thông tin tài khoản, bảo vệ các trang quản trị khi chưa đăng nhập, trang Admin Dashboard và chức năng đăng xuất.	Thử đăng nhập đúng/sai thông tin; truy cập trực tiếp đường dẫn quản trị khi chưa đăng nhập; đăng xuất và kiểm tra quyền truy cập lại.


2. Chi tiết các thay đổi đã thực hiện
2.1. Hoàn thiện ba trạng thái dữ liệu cho S4
Vấn đề: Giao diện chưa có đủ minh chứng thể hiện ba trạng thái dữ liệu theo yêu cầu S4.

Thay đổi đã thực hiện:
- Loading: Hiển thị thông báo/trạng thái đang tải trong thời gian chờ dữ liệu từ API.
- Empty: Hiển thị thông báo phù hợp khi API trả về danh sách rỗng hoặc không có dữ liệu khảo sát phù hợp.
- Error: Hiển thị thông báo khi xảy ra lỗi tải dữ liệu và cung cấp chức năng thử lại.
- Chuẩn hóa việc hiển thị trạng thái để người dùng phân biệt được quá trình tải, dữ liệu rỗng và lỗi hệ thống.
Phạm vi ảnh hưởng:
- frontend/src/components/DataState.jsx
- Các trang React sử dụng component trạng thái dữ liệu.
- Các phần gọi API và xử lý dữ liệu tương ứng.
Cách kiểm chứng:
1. Mở trang có sử dụng dữ liệu từ API và quan sát trạng thái Loading trong lúc chờ phản hồi.
2. Tạo tình huống API trả về danh sách rỗng và xác nhận giao diện hiển thị Empty.
3. Tạo tình huống API không truy cập được hoặc trả về lỗi và xác nhận giao diện hiển thị Error.
4. Kiểm tra chức năng thử lại sau khi lỗi.
5. Lưu ảnh chụp riêng cho từng trạng thái và đưa vào phần minh chứng S4 của báo cáo.
Minh chứng: Bổ sung đường dẫn ảnh chụp thực tế trong repository tại đây nếu tên file hoặc vị trí lưu thay đổi:
- Loading: [đường dẫn ảnh Loading]
- Empty: [đường dẫn ảnh Empty]
- Error: [đường dẫn ảnh Error]
2.2. Hoàn thiện tài liệu và quá trình kiểm thử
Vấn đề: Phần kiểm thử trong báo cáo BT2 còn ngắn, chưa thể hiện đầy đủ việc chuẩn bị, thực thi và đánh giá kết quả.

Thay đổi đã thực hiện:
- Hoàn thiện Test Plan để xác định mục tiêu, phạm vi, phương pháp, môi trường và điều kiện kiểm thử.
- Bổ sung Test Report để ghi nhận test case đã thực hiện, kết quả mong đợi, kết quả thực tế và trạng thái PASS/FAIL.
- Bổ sung Bug Log để quản lý lỗi phát hiện trong quá trình kiểm thử, bao gồm mức độ, mô tả, trạng thái xử lý và commit liên quan khi có.
- Bổ sung minh chứng chạy kiểm thử thực tế.
- Phân biệt test case đã thiết kế với test case đã thực sự chạy; chỉ ghi nhận kết quả dựa trên lần thực thi thực tế.
Phạm vi ảnh hưởng:
- docs/ – Test Plan.
- docs/ – Test Report.
- docs/ – Bug Log.
- Các file kiểm thử trong tests/ và tài liệu minh chứng liên quan.
Cách kiểm chứng:
1. Mở Test Plan và xác nhận phạm vi kiểm thử phù hợp với chức năng hiện có.
2. Đối chiếu từng test case trong Test Report với kết quả chạy thực tế.
3. Kiểm tra tổng số test case đã chạy, số PASS và số FAIL được tính từ kết quả thực tế.
4. Đối chiếu các lỗi FAIL với Bug Log và commit sửa lỗi nếu đã xử lý.
5. Kiểm tra ảnh chụp hoặc log thực thi được lưu trong repository.
Minh chứng: Điền đường dẫn chính xác đến các tài liệu trong repository:
- Test Plan: [đường dẫn file Test Plan]
- Test Report: [đường dẫn file Test Report]
- Bug Log: [đường dẫn file Bug Log]
2.3. Chuẩn hóa repository và loại bỏ node_modules
Vấn đề: Repository chứa thư mục frontend/node_modules, làm tăng dung lượng repository và không cần thiết khi chia sẻ mã nguồn.

Thay đổi đã thực hiện:
- Bổ sung quy tắc node_modules/ vào .gitignore.
- Loại bỏ frontend/node_modules khỏi Git tracking.
- Giữ lại package.json và package-lock.json để tái tạo môi trường cài đặt.
- Không đưa các thư viện phụ thuộc đã cài đặt vào repository.
Phạm vi ảnh hưởng:
- .gitignore
- frontend/package.json
- frontend/package-lock.json
- Repository GitHub.
Cách kiểm chứng:
- Kiểm tra nội dung .gitignore có quy tắc node_modules/.
- Chạy git ls-files và xác nhận không còn file thuộc node_modules được theo dõi.
- Clone repository hoặc mở source code trên môi trường mới, chạy npm install và npm run dev để kiểm tra khả năng cài đặt và khởi chạy.
2.4. Bổ sung chức năng đăng nhập Admin
Vấn đề: Hệ thống chưa có màn hình đăng nhập và chưa có luồng điều hướng riêng cho khu vực quản trị.

Thay đổi đã thực hiện:
- Bổ sung trang đăng nhập Admin.
- Kiểm tra email và mật khẩu trước khi cho phép truy cập.
- Thông tin đăng nhập demo được cấu hình theo yêu cầu:
  - Email: admin@gmail.com
  - Mật khẩu: 123123
- Bổ sung trạng thái đăng nhập để duy trì phiên truy cập trên trình duyệt.
- Bảo vệ các đường dẫn quản trị: người dùng chưa đăng nhập sẽ được chuyển về trang Login.
- Bổ sung Admin Dashboard để lựa chọn ba chức năng đã thiết kế.
- Bổ sung chức năng đăng xuất và xóa trạng thái đăng nhập.
Ba chức năng trên Admin Dashboard:
STT	Chức năng	Đường dẫn
1	Báo cáo tổng quan CSAT/NPS	/
2	Báo cáo kỹ thuật viên	/technicians
3	Chi tiết phiếu khảo sát	/surveys/:id


Phạm vi ảnh hưởng:
- frontend/src/App.jsx
- frontend/src/components/Layout.jsx (nếu có tích hợp điều hướng/đăng xuất)
- frontend/src/styles.css
- Các trang hiện có được giữ lại và truy cập thông qua Admin Dashboard.
Cách kiểm chứng:
1. Truy cập ứng dụng khi chưa đăng nhập và xác nhận được chuyển đến trang Login.
2. Nhập sai email hoặc mật khẩu và xác nhận hệ thống không cho đăng nhập.
3. Nhập đúng tài khoản demo và xác nhận chuyển đến Admin Dashboard.
4. Chọn lần lượt ba chức năng và xác nhận điều hướng đúng trang.
5. Thử truy cập trực tiếp các đường dẫn quản trị khi chưa đăng nhập.
6. Nhấn Đăng xuất và xác nhận hệ thống quay về Login, không thể tiếp tục truy cập trang quản trị nếu chưa đăng nhập lại.
Lưu ý kỹ thuật: Cơ chế đăng nhập hiện tại sử dụng thông tin demo cố định ở phía frontend và localStorage, phù hợp mục đích minh họa/kiểm thử đồ án. Đây chưa phải cơ chế xác thực an toàn cho môi trường triển khai thực tế; hệ thống thực tế cần xác thực và phân quyền ở backend.
3. Các thay đổi thiết kế đã thực hiện từ BT1 sang BT2
3.1. Bổ sung xóa mềm cho khảo sát
- Thay đổi: Bổ sung trường is_deleted vào bảng SURVEY_RESPONSE và chuyển chức năng DELETE sang xóa mềm.
- Lý do: Bảo toàn dữ liệu lịch sử khảo sát, phù hợp với yêu cầu lưu trữ dữ liệu.
- Ảnh hưởng: src/models.py, src/repositories/survey_repository.py, src/services/survey_service.py, src/routes/report_routes.py và migration liên quan.
- Kiểm chứng: Thực hiện thao tác xóa, kiểm tra bản ghi được đánh dấu xóa mềm và không còn xuất hiện trong danh sách truy vấn thông thường.
3.2. Bổ sung CRUD ServiceCenter
- Thay đổi: Bổ sung API tạo, đọc, cập nhật và xóa danh mục trung tâm bảo hành.
- Lý do: Đáp ứng yêu cầu BT2 về CRUD cho các thực thể nghiệp vụ.
- Ảnh hưởng: src/repositories/service_center_repository.py, src/services/service_center_service.py, src/routes/service_center_routes.py, src/__init__.py và API Contract.
- Kiểm chứng: Gửi request API tương ứng với các thao tác Create, Read, Update, Delete và kiểm tra dữ liệu trả về cũng như dữ liệu trong cơ sở dữ liệu.
3.3. Các nội dung đã điều chỉnh theo phản hồi BT1
- Bổ sung chú thích ký hiệu cho sơ đồ Use Case, kiến trúc và ERD.
- Điều chỉnh cách trình bày sơ đồ để nội dung dễ đọc hơn.
- Bổ sung dữ liệu cần thiết phục vụ tính toán CSAT/NPS và hoàn thiện mô tả dữ liệu liên quan.
- Bổ sung thông tin GitHub, track và thông tin cam kết trong tài liệu theo yêu cầu.
- Bổ sung file nguồn và cập nhật cách quản lý commit cho các thay đổi.
4. Kiểm tra tổng thể sau khi hoàn thiện
STT	Hạng mục	Kết quả cần xác nhận
1	Đăng nhập Admin	Đăng nhập đúng/sai hoạt động theo yêu cầu
2	Bảo vệ đường dẫn	Chưa đăng nhập không truy cập được trang quản trị
3	Admin Dashboard	Hiển thị và điều hướng đủ ba chức năng
4	Đăng xuất	Xóa trạng thái đăng nhập và quay về Login
5	S4 – Loading	Có hiển thị và ảnh minh chứng
6	S4 – Empty	Có hiển thị và ảnh minh chứng
7	S4 – Error	Có hiển thị, thử lại và ảnh minh chứng
8	Test Plan/Test Report/Bug Log	Có tài liệu và kết quả kiểm thử thực tế
9	Git repository	Không còn theo dõi node_modules
10	Backend/API	Các API và CRUD đã hoàn thiện được kiểm tra
11	Database/Migration	Migration hoạt động và dữ liệu phù hợp
12	Giao diện hiện có	Ba trang nghiệp vụ vẫn truy cập và hoạt động
