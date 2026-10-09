# API Contract -- Track SE

## Hệ thống CSAT/NPS -- Smart CRM Mekong Mobile

-   **Luồng:** L8 -- Khảo sát hài lòng CSAT/NPS
-   **Track:** SE
-   **Phiên bản:** 1.0 -- tài liệu thiết kế cho BT1, chưa phải API đã
    triển khai
-   **Base path:** `/api/v1`
-   **Định dạng:** JSON qua HTTPS

> **Lưu ý:** Case study mô tả phản hồi khảo sát sau khi phiếu được đóng,
> với thang điểm 1--5 và nhận xét. Các endpoint bên dưới là thiết kế đề
> xuất cho L8, không phải URL được quy định sẵn trong tài liệu nghiệp
> vụ. Vì yêu cầu L8 có cả CSAT và NPS, trường `nps_score` được đề xuất
> bổ sung; cần xác nhận với giảng viên/nghiệp vụ cách thu thập NPS và
> công thức tính trước khi triển khai.

## 1. Quy ước chung

### 1.1. Xác thực và phân quyền

-   Các API báo cáo yêu cầu người dùng đã đăng nhập.
-   Server lấy vai trò và phạm vi trung tâm từ thông tin phân quyền phía
    server; không tin `role` hoặc `center_id` do client gửi để quyết
    định quyền.
-   **Marketing:** xem báo cáo theo thời gian và theo trung tâm trong
    phạm vi được cấp.
-   **Quản lý trung tâm:** chỉ xem dữ liệu của trung tâm được phân
    quyền.
-   **Ban giám đốc:** xem báo cáo tổng hợp toàn công ty theo quyền được
    cấp.
-   Theo QT-15/NFR4, số điện thoại khách hàng phải được che khi hiển thị
    cho Quản lý trung tâm và Ban giám đốc. Không trả số điện thoại đầy
    đủ trong các response báo cáo.

### 1.2. Quy tắc dữ liệu

1.  Chỉ tổng hợp các phản hồi khảo sát hợp lệ thuộc phạm vi L8.
2.  Theo QT-10, khảo sát chỉ liên quan đến phiếu bảo hành ở trạng thái
    **ĐÃ ĐÓNG**; mỗi phiếu có tối đa một phản hồi khảo sát.
3.  Theo QT-14, mọi truy vấn của Quản lý trung tâm phải giới hạn theo
    trung tâm được phân quyền.
4.  API trong tài liệu này chỉ phục vụ **đọc báo cáo**; không tạo, sửa
    hoặc xóa phiếu khảo sát.
5.  Dữ liệu lịch sử không bị xóa vật lý theo QT-13.
6.  Các trường `center_id`, `technician_id`, `ticket_id`, `response_id`
    dùng kiểu số nguyên theo ERD đề xuất.

### 1.3. Quy tắc request

-   Ngày sử dụng định dạng `YYYY-MM-DD`.
-   `start_date` và `end_date` bắt buộc ở endpoint có lọc thời gian,
    tính cả ngày bắt đầu và ngày kết thúc.
-   `start_date` không được lớn hơn `end_date`.
-   Với endpoint danh sách có phân trang: `page` mặc định `1`, giá trị
    tối thiểu `1`; `page_size` mặc định `25`, giới hạn từ `1` đến `100`.
-   Các con số trong response mẫu chỉ minh họa cấu trúc, không phải dữ
    liệu thực tế.

### 1.4. Quy ước chỉ số

-   `response_count`: số phản hồi khảo sát hợp lệ trong phạm vi truy
    vấn.
-   `csat_score`: điểm/tỷ lệ CSAT theo công thức được thống nhất trong
    SRS.
-   `nps_score`: điểm NPS theo công thức được thống nhất trong SRS. Nếu
    chưa có dữ liệu NPS hoặc chưa chốt cách thu thập, trả `null`; không
    tự suy ra NPS từ thang điểm CSAT 1--5.
-   Tài liệu này không tự đặt công thức CSAT/NPS vì cần thống nhất với
    quy tắc nghiệp vụ.

------------------------------------------------------------------------

## 2. API-01 --- Xem CSAT/NPS theo thời gian

  Thuộc tính      Nội dung
  --------------- --------------------------------------------------------
  Method / Path   `GET /api/v1/reports/csat-nps/by-time`
  User Story      US1 -- Xem CSAT/NPS theo thời gian (**MUST**)
  Use Case        UC1 -- Xem CSAT/NPS theo thời gian
  Actor           Marketing
  Mục đích        Trả kết quả CSAT/NPS trong khoảng thời gian được chọn.
  Quyền           Đã đăng nhập và có quyền xem báo cáo.

**Query parameters**

  -----------------------------------------------------------------------
  Tên               Kiểu              Bắt buộc          Quy tắc
  ----------------- ----------------- ----------------- -----------------
  `start_date`      date              Có                Định dạng
                                                        `YYYY-MM-DD`

  `end_date`        date              Có                Định dạng
                                                        `YYYY-MM-DD`,
                                                        không nhỏ hơn
                                                        `start_date`
  -----------------------------------------------------------------------

**Request mẫu**

``` http
GET /api/v1/reports/csat-nps/by-time?start_date=2026-09-01&end_date=2026-09-30
Accept: application/json
Authorization: Bearer <access_token>
```

**Response `200 OK`**

``` json
{
  "data": {
    "start_date": "2026-09-01",
    "end_date": "2026-09-30",
    "response_count": 320,
    "csat_score": 92.5,
    "nps_score": 48.0
  }
}
```

------------------------------------------------------------------------

## 3. API-02 --- Xem CSAT/NPS theo trung tâm

  Thuộc tính      Nội dung
  --------------- -----------------------------------------------
  Method / Path   `GET /api/v1/reports/csat-nps/by-center`
  User Story      US2 -- Xem CSAT/NPS theo trung tâm (**MUST**)
  Use Case        UC2 -- Xem CSAT/NPS theo trung tâm
  Actor           Marketing
  Mục đích        Trả kết quả của trung tâm được chọn.

**Query parameters**

  -----------------------------------------------------------------------
  Tên               Kiểu              Bắt buộc          Quy tắc
  ----------------- ----------------- ----------------- -----------------
  `center_id`       integer           Có                Phải tồn tại và
                                                        người dùng có
                                                        quyền xem

  `start_date`      date              Có                Định dạng
                                                        `YYYY-MM-DD`

  `end_date`        date              Có                Định dạng
                                                        `YYYY-MM-DD`,
                                                        không nhỏ hơn
                                                        `start_date`
  -----------------------------------------------------------------------

**Request mẫu**

``` http
GET /api/v1/reports/csat-nps/by-center?center_id=1&start_date=2026-09-01&end_date=2026-09-30
Accept: application/json
Authorization: Bearer <access_token>
```

**Response `200 OK`**

``` json
{
  "data": {
    "center_id": 1,
    "center_name": "Trung tâm A",
    "start_date": "2026-09-01",
    "end_date": "2026-09-30",
    "response_count": 85,
    "csat_score": 91.2,
    "nps_score": 45.0
  }
}
```

Nếu trung tâm hợp lệ nhưng không có khảo sát trong kỳ, trả `200 OK`,
`response_count: 0`, và các chỉ số không có dữ liệu là `null`. Giao diện
hiển thị thông báo **"Không có dữ liệu khảo sát."**

------------------------------------------------------------------------

## 4. API-03 --- Quản lý xem CSAT/NPS của trung tâm được phân quyền

  Thuộc tính      Nội dung
  --------------- -------------------------------------------------------
  Method / Path   `GET /api/v1/reports/csat-nps/my-center`
  User Story      US3 -- Quản lý xem CSAT/NPS của trung tâm (**MUST**)
  Use Case        UC3 -- Xem CSAT/NPS của trung tâm
  Actor           Quản lý trung tâm
  Mục đích        Trả kết quả của trung tâm mà Quản lý được phân quyền.

**Query parameters:** `start_date` và `end_date` (date, bắt buộc;
`start_date <= end_date`).

Endpoint này **không nhận `center_id` từ client** để xác định phạm vi.
Server lấy trung tâm từ thông tin phân quyền đã xác thực.

**Request mẫu**

``` http
GET /api/v1/reports/csat-nps/my-center?start_date=2026-09-01&end_date=2026-09-30
Accept: application/json
Authorization: Bearer <access_token>
```

**Response `200 OK`**

``` json
{
  "data": {
    "center_id": 1,
    "center_name": "Trung tâm A",
    "start_date": "2026-09-01",
    "end_date": "2026-09-30",
    "response_count": 85,
    "csat_score": 91.2,
    "nps_score": 45.0
  }
}
```

------------------------------------------------------------------------

## 5. API-04 --- Xem CSAT/NPS theo kỹ thuật viên

  ----------------------------------------------------------------------------------
  Thuộc tính                          Nội dung
  ----------------------------------- ----------------------------------------------
  Method / Path                       `GET /api/v1/reports/csat-nps/by-technician`

  User Story                          US4 -- Xem CSAT/NPS theo kỹ thuật viên
                                      (**MUST**)

  Use Case                            UC4 -- Xem CSAT/NPS theo kỹ thuật viên

  Actor                               Quản lý trung tâm

  Mục đích                            Tổng hợp CSAT/NPS theo kỹ thuật viên trong
                                      trung tâm được phân quyền.
  ----------------------------------------------------------------------------------

**Query parameters**

  -----------------------------------------------------------------------
  Tên               Kiểu              Bắt buộc          Quy tắc
  ----------------- ----------------- ----------------- -----------------
  `start_date`      date              Có                Định dạng
                                                        `YYYY-MM-DD`

  `end_date`        date              Có                Định dạng
                                                        `YYYY-MM-DD`,
                                                        không nhỏ hơn
                                                        `start_date`

  `page`            integer           Không             Mặc định `1`, tối
                                                        thiểu `1`

  `page_size`       integer           Không             Mặc định `25`,
                                                        giới hạn `1–100`
  -----------------------------------------------------------------------

**Request mẫu**

``` http
GET /api/v1/reports/csat-nps/by-technician?start_date=2026-09-01&end_date=2026-09-30&page=1&page_size=25
Accept: application/json
Authorization: Bearer <access_token>
```

**Response `200 OK`**

``` json
{
  "data": [
    {
      "technician_id": 1,
      "technician_name": "Kỹ thuật viên A",
      "response_count": 30,
      "csat_score": 93.0,
      "nps_score": 50.0
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 25,
    "total_items": 1
  }
}
```

-   Server bắt buộc lọc theo trung tâm mà Quản lý được phân quyền trước
    khi tổng hợp.
-   Nếu Quản lý cố truy cập dữ liệu của trung tâm khác, trả
    `403 Forbidden` và không tiết lộ dữ liệu đó.
-   Nếu không có dữ liệu khảo sát hợp lệ, trả danh sách rỗng và
    `total_items: 0`.

------------------------------------------------------------------------

## 6. API-05 --- Xem báo cáo CSAT/NPS tổng hợp toàn công ty

  Thuộc tính      Nội dung
  --------------- --------------------------------------------
  Method / Path   `GET /api/v1/reports/csat-nps/summary`
  User Story      US5 -- Xem báo cáo tổng hợp (**MUST**)
  Use Case        UC5 -- Xem báo cáo CSAT/NPS tổng hợp
  Actor           Ban giám đốc
  Mục đích        Trả chỉ số CSAT/NPS tổng hợp toàn công ty.

**Query parameters:** `start_date` và `end_date` (date, bắt buộc;
`start_date <= end_date`).

**Request mẫu**

``` http
GET /api/v1/reports/csat-nps/summary?start_date=2026-09-01&end_date=2026-09-30
Accept: application/json
Authorization: Bearer <access_token>
```

**Response `200 OK`**

``` json
{
  "data": {
    "scope": "company",
    "start_date": "2026-09-01",
    "end_date": "2026-09-30",
    "response_count": 1200,
    "csat_score": 90.8,
    "nps_score": 42.5
  }
}
```

------------------------------------------------------------------------

## 7. Quy tắc dùng chung --- US7 kiểm soát phạm vi dữ liệu

US7 không nhất thiết là endpoint riêng. Đây là quy tắc phân quyền áp
dụng cho các API báo cáo.

-   Quản lý trung tâm chỉ nhận dữ liệu thuộc trung tâm được phân quyền.
-   Ban giám đốc được xem dữ liệu tổng hợp toàn công ty.
-   Việc kiểm tra quyền phải diễn ra ở phía server trước khi trả dữ
    liệu.
-   Không dựa vào `center_id` do client gửi để quyết định quyền của Quản
    lý.

**Response khi bị từ chối --- `403 Forbidden`**

``` json
{
  "error": {
    "code": "FORBIDDEN_CENTER_SCOPE",
    "message": "Bạn không có quyền truy cập dữ liệu của trung tâm này."
  }
}
```

------------------------------------------------------------------------

## 8. Quy tắc dùng chung --- US8 che số điện thoại khách hàng

US8 là quy tắc bảo vệ dữ liệu, không phải endpoint độc lập. Nếu response
báo cáo có trường số điện thoại, Service Layer phải che số điện thoại
trước khi trả về giao diện theo QT-15/NFR4.

**Ví dụ**

``` json
{
  "customer_id": 1,
  "customer_phone": "******678"
}
```

Ví dụ chỉ minh họa dạng đã che. Không trả số điện thoại đầy đủ cho vai
trò phải áp dụng masking. Nếu API báo cáo không cần số điện thoại, nên
không đưa trường này vào response.

------------------------------------------------------------------------

## 9. API mở rộng --- US6 (SHOULD)

  ---------------------------------------------------------------------------------------
  Thuộc tính                          Nội dung
  ----------------------------------- ---------------------------------------------------
  Method / Path                       `GET /api/v1/reports/csat-nps/by-center-and-time`

  User Story                          US6 -- Xem CSAT/NPS theo trung tâm và thời gian
                                      (**SHOULD**)

  Use Case                            UC6 -- Xem CSAT/NPS theo trung tâm và thời gian

  Actor                               Ban giám đốc

  Mục đích                            So sánh kết quả theo trung tâm trong khoảng thời
                                      gian.
  ---------------------------------------------------------------------------------------

**Query parameters:** `start_date` và `end_date` (date, bắt buộc;
`start_date <= end_date`).

**Request mẫu**

``` http
GET /api/v1/reports/csat-nps/by-center-and-time?start_date=2026-09-01&end_date=2026-09-30
Accept: application/json
Authorization: Bearer <access_token>
```

**Response `200 OK`**

``` json
{
  "data": [
    {
      "center_id": 1,
      "center_name": "Trung tâm A",
      "response_count": 85,
      "csat_score": 91.2,
      "nps_score": 45.0
    },
    {
      "center_id": 2,
      "center_name": "Trung tâm B",
      "response_count": 72,
      "csat_score": 89.5,
      "nps_score": 40.0
    }
  ],
  "period": {
    "start_date": "2026-09-01",
    "end_date": "2026-09-30"
  }
}
```

------------------------------------------------------------------------

## 10. Validation và mã lỗi

  -----------------------------------------------------------------------------------
  HTTP status                   Error code                 Điều kiện
  ----------------------------- -------------------------- --------------------------
  `200 OK`                      ---                        Truy vấn thành công; dữ
                                                           liệu có thể rỗng.

  `400 Bad Request`             `INVALID_DATE_FORMAT`      Ngày không đúng định dạng
                                                           `YYYY-MM-DD`.

  `400 Bad Request`             `INVALID_DATE_RANGE`       Thiếu ngày bắt buộc hoặc
                                                           `start_date > end_date`.

  `400 Bad Request`             `INVALID_PAGINATION`       `page < 1` hoặc
                                                           `page_size` ngoài giới hạn
                                                           `1–100`.

  `401 Unauthorized`            `UNAUTHENTICATED`          Chưa đăng nhập hoặc thông
                                                           tin xác thực không hợp
                                                           lệ/hết hạn.

  `403 Forbidden`               `FORBIDDEN`                Không có quyền sử dụng
                                                           endpoint.

  `403 Forbidden`               `FORBIDDEN_CENTER_SCOPE`   Quản lý yêu cầu dữ liệu
                                                           ngoài trung tâm được phân
                                                           quyền.

  `404 Not Found`               `CENTER_NOT_FOUND`         `center_id` không tồn tại
                                                           ở endpoint nhận mã trung
                                                           tâm.

  `500 Internal Server Error`   `INTERNAL_ERROR`           Lỗi hệ thống; không trả
                                                           stack trace hoặc thông tin
                                                           nhạy cảm cho client.
  -----------------------------------------------------------------------------------

**Response lỗi mẫu**

``` json
{
  "error": {
    "code": "INVALID_DATE_RANGE",
    "message": "Ngày bắt đầu phải nhỏ hơn hoặc bằng ngày kết thúc."
  }
}
```

------------------------------------------------------------------------

## 11. Bảng truy vết Endpoint ↔ User Story ↔ Use Case

  --------------------------------------------------------------------------------------------------
  API / Quy tắc                                User Story        Use Case / yêu    MoSCoW
                                                                 cầu               
  -------------------------------------------- ----------------- ----------------- -----------------
  API-01 `GET /reports/csat-nps/by-time`       US1 -- Xem        UC1 -- Xem        MUST
                                               CSAT/NPS theo     CSAT/NPS theo     
                                               thời gian         thời gian         

  API-02 `GET /reports/csat-nps/by-center`     US2 -- Xem        UC2 -- Xem        MUST
                                               CSAT/NPS theo     CSAT/NPS theo     
                                               trung tâm         trung tâm         

  API-03 `GET /reports/csat-nps/my-center`     US3 -- Quản lý    UC3 -- Xem        MUST
                                               xem CSAT/NPS của  CSAT/NPS của      
                                               trung tâm         trung tâm         

  API-04 `GET /reports/csat-nps/by-technician` US4 -- Xem        UC4 -- Xem        MUST
                                               CSAT/NPS theo kỹ  CSAT/NPS theo kỹ  
                                               thuật viên        thuật viên        

  API-05 `GET /reports/csat-nps/summary`       US5 -- Xem báo    UC5 -- Xem báo    MUST
                                               cáo tổng hợp      cáo CSAT/NPS tổng 
                                                                 hợp               

  Quy tắc phân quyền dùng chung                US7 -- Kiểm soát  UC7 -- Kiểm soát  MUST
                                               phạm vi dữ liệu   phạm vi dữ liệu   

  Quy tắc masking dùng chung                   US8 -- Che số     QT-15 / NFR4      MUST
                                               điện thoại khách                    
                                               hàng                                

  API-06                                       US6 -- Xem        UC6 -- Xem        SHOULD
  `GET /reports/csat-nps/by-center-and-time`   CSAT/NPS theo     CSAT/NPS theo     
                                               trung tâm và thời trung tâm và thời 
                                               gian              gian              
  --------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 12. Liên hệ với kiến trúc

-   **Presentation Layer:** gọi API báo cáo và hiển thị kết quả.
-   **Application/API Layer:** nhận request, xác thực và kiểm tra quyền
    truy cập.
-   **Service Layer:** lọc dữ liệu, tổng hợp CSAT/NPS, kiểm soát phạm vi
    trung tâm và che số điện thoại khi cần.
-   **Data Access Layer:** truy vấn dữ liệu theo yêu cầu của Service
    Layer.
-   **Database:** cung cấp dữ liệu từ các nhóm `Survey_Response`,
    `Ticket`, `Technician`, `Service_Center`, `Customer` và `Dim_Date`
    theo ERD của dự án.

SMS/Email marketing, xử lý sửa chữa, phân công kỹ thuật viên và dự đoán
AI nằm ngoài phạm vi L8 theo kiến trúc hiện tại.

## 13. Giả định và điểm cần đồng bộ trước khi nộp

1.  URL endpoint và schema JSON là thiết kế đề xuất; tài liệu nghiệp vụ
    không quy định URL API cụ thể.
2.  `center_id`, `technician_id` và `customer_id` trong ví dụ dùng kiểu
    số nguyên để thống nhất với ERD đề xuất. Nếu ERD cuối cùng đổi tên
    hoặc kiểu dữ liệu, cần cập nhật API contract tương ứng.
3.  Case study nêu khảo sát hài lòng thang điểm 1--5 và nhận xét.
    `nps_score` là phần mở rộng đề xuất để đáp ứng yêu cầu báo cáo NPS;
    cần xác nhận cách thu thập điểm NPS (thường là thang 0--10) trước
    khi triển khai.
4.  Công thức tính `csat_score` và `nps_score` phải được thống nhất
    trong SRS/nghiệp vụ; tài liệu này không tự đặt công thức.
5.  Các số liệu response mẫu chỉ minh họa cấu trúc, không phải số liệu
    thật.
6.  Nếu SRS cuối cùng thay đổi mã/tên User Story hoặc Use Case, cập nhật
    bảng truy vết tại Mục 11.
7.  Đây là hợp đồng API ở mức thiết kế cho BT1; chưa khẳng định endpoint
    đã được lập trình hoặc kiểm thử.
