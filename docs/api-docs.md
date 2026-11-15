# API Documentation – Smart CRM CSAT/NPS

## 1. Overview

### 1.1. Purpose

This document describes the REST API implemented in the Smart CRM – CSAT/NPS prototype for Mekong Mobile.

The API supports:
- Checking backend service availability.
- Managing customer satisfaction survey responses.
- Managing service centers.
- Generating CSAT/NPS reports.

### 1.2. Technology

| Component | Technology |
|---|---|
| Backend framework | Flask |
| ORM | Flask-SQLAlchemy |
| Database migration | Flask-Migrate |
| Database | PostgreSQL |
| API format | REST |
| Data format | JSON |

### 1.3. Base URL

Local development:

`http://127.0.0.1:5000`

All request and response bodies use JSON where applicable.

### 1.4. Authentication

**Authentication status: Not implemented in the current backend.**

The current Flask API does not contain backend authentication middleware or role-based authorization.

The frontend admin login is a demonstration feature and does not secure direct API requests.

Therefore:
- API endpoints currently do not require an access token.
- The backend does not enforce the manager's assigned service-center scope.
- The backend does not enforce role-based access for Marketing, Service Center Managers, or the Board of Directors.

These are known security limitations and must not be described as implemented features.

---

## 2. Health API

### 2.1. Check API health

**Method:** GET

**Endpoint:** `/health`

**Description:** Checks whether the Flask backend is running.

**Authentication:** Not required.

**Parameters:** None.

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "status": "ok",
  "message": "L8 API is running"
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 500 | Internal server error |

**Limitations:** This endpoint confirms that the health route responds. It does not independently verify database availability.

---

## 3. Survey API

Base path: `/api/surveys`

### 3.1. Get all surveys

**Method:** GET

**Endpoint:** `/api/surveys`

**Description:** Retrieves the survey responses returned by the survey repository.

**Authentication:** Not required.

**Parameters:** None.

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "data": [
    {
      "response_id": 1,
      "ticket_id": 1001,
      "date_id": 1,
      "score": 5,
      "nps_score": 9,
      "comment": "Good service",
      "responded_at": "2026-10-01T10:00:00"
    }
  ]
}
```

The values above illustrate the response structure. Replace this example with the actual output from your running database before submitting.

**Error codes:**

| HTTP status | Description |
|---|---|
| 500 | Internal server error |

**Limitations:** The route does not implement pagination or query filters.

### 3.2. Get survey by ID

**Method:** GET

**Endpoint:** `/api/surveys/{response_id}`

**Description:** Retrieves one survey response by its response ID.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| response_id | Integer | Yes | Survey response ID |

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "data": {
    "response_id": 1,
    "ticket_id": 1001,
    "date_id": 1,
    "score": 5,
    "nps_score": 9,
    "comment": "Good service",
    "responded_at": "2026-10-01T10:00:00"
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 404 | Survey response not found |
| 500 | Internal server error |

### 3.3. Create a survey

**Method:** POST

**Endpoint:** `/api/surveys`

**Description:** Creates a survey response associated with a closed warranty ticket.

**Authentication:** Not required.

**Parameters:** None.

**Request headers:**

`Content-Type: application/json`

**Request body:**

| Field | Type | Required | Validation |
|---|---|---|---|
| ticket_id | Integer | Yes | Greater than 0 |
| date_id | Integer | Yes | Greater than 0 |
| score | Integer | Yes | From 1 to 5 |
| nps_score | Integer | Yes | From 0 to 10 |
| comment | String or null | No | Must be a string or null |

**Request example:**

```json
{
  "ticket_id": 1001,
  "date_id": 1,
  "score": 5,
  "nps_score": 9,
  "comment": "Good service"
}
```

Use an existing ticket ID and date ID from your database when testing.

**Success response – 201 Created:**

```json
{
  "message": "Tạo khảo sát thành công.",
  "data": {
    "response_id": 1,
    "ticket_id": 1001,
    "date_id": 1,
    "score": 5,
    "nps_score": 9,
    "comment": "Good service",
    "responded_at": "2026-10-01T10:00:00"
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid JSON, missing fields, invalid types, invalid score, invalid ticket/date, ticket not closed, or duplicate survey |
| 500 | Internal server error |

**Business rules:**
- The ticket must exist.
- The ticket status must be `CLOSED` or `ĐÃ ĐÓNG`.
- The date record must exist.
- Each ticket can have only one survey response, including previously soft-deleted responses.

### 3.4. Update a survey

**Method:** PUT

**Endpoint:** `/api/surveys/{response_id}`

**Description:** Updates an existing survey response.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| response_id | Integer | Yes | Survey response ID |

**Request body:** Uses the same fields and validation rules as Create a survey.

**Request example:**

```json
{
  "ticket_id": 1001,
  "date_id": 1,
  "score": 4,
  "nps_score": 8,
  "comment": "Service was good"
}
```

**Success response – 200 OK:**

```json
{
  "message": "Cập nhật thành công.",
  "data": {
    "response_id": 1,
    "ticket_id": 1001,
    "date_id": 1,
    "score": 4,
    "nps_score": 8,
    "comment": "Service was good",
    "responded_at": "2026-10-01T10:00:00"
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid request or business-rule violation |
| 404 | Survey response not found |
| 500 | Internal server error |

### 3.5. Delete a survey

**Method:** DELETE

**Endpoint:** `/api/surveys/{response_id}`

**Description:** Soft-deletes a survey response.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| response_id | Integer | Yes | Survey response ID |

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "message": "Xóa khảo sát thành công."
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 404 | Survey response not found |
| 500 | Internal server error |

**Limitations:** The current implementation uses soft deletion rather than physically deleting the database record.

---

## 4. Service Center API

Base path: `/api/service-centers`

### 4.1. Get all service centers

**Method:** GET

**Endpoint:** `/api/service-centers`

**Description:** Retrieves all service centers.

**Authentication:** Not required.

**Parameters:** None.

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "data": [
    {
      "center_id": 1,
      "center_name": "Example Service Center"
    }
  ]
}
```

Replace the example with actual database output.

**Error codes:**

| HTTP status | Description |
|---|---|
| 500 | Internal server error |

### 4.2. Get service center by ID

**Method:** GET

**Endpoint:** `/api/service-centers/{center_id}`

**Description:** Retrieves a service center by its ID.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | Integer | Yes | Service center ID |

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "data": {
    "center_id": 1,
    "center_name": "Example Service Center"
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 404 | Service center not found |
| 500 | Internal server error |

### 4.3. Create a service center

**Method:** POST

**Endpoint:** `/api/service-centers`

**Description:** Creates a new service center.

**Authentication:** Not required.

**Request headers:**

`Content-Type: application/json`

**Request body:**

| Field | Type | Required | Validation |
|---|---|---|---|
| center_name | String | Yes | Non-empty after trimming; maximum 100 characters |

**Request example:**

```json
{
  "center_name": "Example Service Center"
}
```

Use a test name that does not conflict with existing database records.

**Success response – 201 Created:**

```json
{
  "message": "Tạo trung tâm thành công.",
  "data": {
    "center_id": 1,
    "center_name": "Example Service Center"
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid request body or center name |
| 409 | Database conflict |
| 500 | Internal server error |

### 4.4. Update a service center

**Method:** PUT

**Endpoint:** `/api/service-centers/{center_id}`

**Description:** Updates an existing service center.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | Integer | Yes | Service center ID |

**Request body:** Uses the same `center_name` validation as Create a service center.

**Request example:**

```json
{
  "center_name": "Updated Service Center"
}
```

**Success response – 200 OK:**

```json
{
  "message": "Cập nhật trung tâm thành công.",
  "data": {
    "center_id": 1,
    "center_name": "Updated Service Center"
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid request body or center name |
| 404 | Service center not found |
| 409 | Database conflict |
| 500 | Internal server error |

### 4.5. Delete a service center

**Method:** DELETE

**Endpoint:** `/api/service-centers/{center_id}`

**Description:** Deletes a service center if it has no linked technicians or warranty tickets.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | Integer | Yes | Service center ID |

**Request body:** None.

**Success response – 200 OK:**

```json
{
  "message": "Xóa trung tâm thành công."
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 404 | Service center not found |
| 409 | Center has linked technicians or warranty tickets |
| 500 | Internal server error |

---

## 5. CSAT/NPS Report API

Base path: `/api/v1/reports/csat-nps`

All report endpoints use GET requests.

### 5.1. Get CSAT/NPS summary

**Method:** GET

**Endpoint:** `/api/v1/reports/csat-nps/summary`

**Description:** Calculates the total number of valid survey responses, average CSAT score, and average NPS score.

**Authentication:** Not required.

**Query parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| startDate | Date string | No | Start date in YYYY-MM-DD format |
| endDate | Date string | No | End date in YYYY-MM-DD format |
| centerId | Integer | No | Positive service center ID |

**Request example:**

`GET /api/v1/reports/csat-nps/summary?startDate=2026-10-01&endDate=2026-10-31`

**Success response – 200 OK:**

```json
{
  "data": {
    "surveyCount": 0,
    "csat": {
      "averageScore": null
    },
    "nps": {
      "score": null,
      "status": "unavailable"
    }
  }
}
```

This is the actual response structure when no valid survey records are found. Values will differ when the database contains matching records.

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid date format, invalid date range, or invalid centerId |
| 500 | Report processing error |

### 5.2. Get CSAT/NPS trend

**Method:** GET

**Endpoint:** `/api/v1/reports/csat-nps/trend`

**Description:** Groups survey metrics by day or month.

**Authentication:** Not required.

**Query parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| startDate | Date string | No | Start date in YYYY-MM-DD format |
| endDate | Date string | No | End date in YYYY-MM-DD format |
| centerId | Integer | No | Positive service center ID |
| groupBy | String | No | `day` or `month`; default is `day` |

**Request example:**

`GET /api/v1/reports/csat-nps/trend?startDate=2026-10-01&endDate=2026-10-31&groupBy=month`

**Success response – 200 OK:**

```json
{
  "data": {
    "items": [
      {
        "period": "2026-10",
        "surveyCount": 0,
        "csat": {
          "averageScore": null
        },
        "nps": {
          "score": null,
          "status": "unavailable"
        }
      }
    ]
  }
}
```

The item above illustrates the response structure. Actual periods and values depend on the database.

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid date, invalid date range, invalid centerId, or invalid groupBy |
| 500 | Report processing error |

### 5.3. Get report by service center

**Method:** GET

**Endpoint:** `/api/v1/reports/csat-nps/centers`

**Description:** Groups survey metrics by service center. The response also includes existing service centers without matching survey responses.

**Authentication:** Not required.

**Query parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| startDate | Date string | No | Start date in YYYY-MM-DD format |
| endDate | Date string | No | End date in YYYY-MM-DD format |
| centerId | Integer | No | Positive service center ID |

**Request example:**

`GET /api/v1/reports/csat-nps/centers?startDate=2026-10-01&endDate=2026-10-31`

**Success response – 200 OK:**

```json
{
  "data": {
    "items": [
      {
        "centerId": 1,
        "centerName": "Example Service Center",
        "surveyCount": 0,
        "csat": {
          "averageScore": null
        },
        "nps": {
          "score": null,
          "status": "unavailable"
        }
      }
    ]
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid date, invalid date range, or invalid centerId |
| 500 | Report processing error |

### 5.4. Get report by technician

**Method:** GET

**Endpoint:** `/api/v1/reports/csat-nps/technicians`

**Description:** Groups survey metrics by technician. Records without a technician ID are excluded.

**Authentication:** Not required.

**Query parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| startDate | Date string | No | Start date in YYYY-MM-DD format |
| endDate | Date string | No | End date in YYYY-MM-DD format |
| centerId | Integer | No | Positive service center ID |

**Request example:**

`GET /api/v1/reports/csat-nps/technicians?startDate=2026-10-01&endDate=2026-10-31`

**Success response – 200 OK:**

```json
{
  "data": {
    "items": [
      {
        "technicianId": 1,
        "technicianName": "Example Technician",
        "centerId": 1,
        "centerName": "Example Service Center",
        "surveyCount": 0,
        "csat": {
          "averageScore": null
        },
        "nps": {
          "score": null,
          "status": "unavailable"
        }
      }
    ]
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid date, invalid date range, or invalid centerId |
| 500 | Report processing error |

### 5.5. Get detailed report by service center

**Method:** GET

**Endpoint:** `/api/v1/reports/csat-nps/centers/{center_id}`

**Description:** Retrieves CSAT/NPS metrics for a specific service center.

**Authentication:** Not required.

**Path parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| center_id | Integer | Yes | Service center ID |

**Query parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| startDate | Date string | No | Start date in YYYY-MM-DD format |
| endDate | Date string | No | End date in YYYY-MM-DD format |
| centerId | Integer | No | Additional center filter applied by the shared report query |

**Request example:**

`GET /api/v1/reports/csat-nps/centers/1?startDate=2026-10-01&endDate=2026-10-31`

**Success response – 200 OK:**

```json
{
  "data": {
    "centerId": 1,
    "centerName": "Example Service Center",
    "surveyCount": 0,
    "csat": {
      "averageScore": null
    },
    "nps": {
      "score": null,
      "status": "unavailable"
    }
  }
}
```

**Error codes:**

| HTTP status | Description |
|---|---|
| 400 | Invalid date, invalid date range, or invalid centerId |
| 404 | Center not found |
| 500 | Report processing error |

---

## 6. Common Report Business Rules

The report APIs apply the following rules in the current implementation:

1. Only survey responses that have not been soft-deleted are included.
2. Only surveys associated with tickets whose status is `CLOSED` or `ĐÃ ĐÓNG` are included.
3. Survey dates are obtained through the `DIM_DATE` relationship.
4. `startDate` and `endDate` are optional filters.
5. If both dates are provided, `startDate` must not be later than `endDate`.
6. `centerId`, when provided, must be a positive integer.
7. The `groupBy` parameter supports `day` and `month`; the default is `day`.
8. CSAT is calculated as the average of `score`.
9. The report's `nps.score` is currently calculated as the average of `nps_score` values on a 0–10 scale. It is not the standard NPS percentage/index formula.
10. When no valid NPS values are available, the response uses `null` and status `unavailable`.

---

## 7. General Error Handling

| HTTP status | Meaning | Current API behavior |
|---|---|---|
| 200 | OK | Request completed successfully |
| 201 | Created | Survey or service center created |
| 400 | Bad Request | Invalid JSON, invalid input, or invalid report filter |
| 404 | Not Found | Requested survey or service center does not exist |
| 409 | Conflict | Service center operation conflicts with linked data or database constraints |
| 500 | Internal Server Error | Unexpected server-side error |

The current routes return error messages using JSON fields named `error` or `message`, depending on the route.

---

## 8. Security and Known Limitations

The following limitations have been identified from the current source code:

| Item | Current status | Description |
|---|---|---|
| Backend authentication | Not implemented | API endpoints do not require login or token authentication |
| Role-based authorization | Not implemented | Backend does not enforce user roles |
| Service-center data scope | Not implemented | Report endpoints do not restrict managers to their assigned center |
| Phone number masking | Not implemented in report authorization flow | Report endpoints currently do not return phone numbers, but there is no role-based masking enforcement |
| Pagination | Not implemented | Survey and service-center list endpoints do not provide pagination |
| Report date filters | Implemented | `startDate` and `endDate` are optional |
| Report soft-delete filter | Implemented | Soft-deleted survey responses are excluded |
| Closed-ticket filter | Implemented | Only `CLOSED` and `ĐÃ ĐÓNG` tickets are included |

These limitations must be considered before deploying the prototype in a production environment.

---

## 9. Source Code References

| API group | Source file |
|---|---|
| Application configuration and health check | `src/__init__.py` |
| Survey endpoints | `src/routes/survey_routes.py` |
| Survey validation and business rules | `src/services/survey_service.py` |
| Service-center endpoints | `src/routes/service_center_routes.py` |
| Service-center validation and business rules | `src/services/service_center_service.py` |
| CSAT/NPS report endpoints | `src/routes/report_routes.py` |
| Database models | `src/models.py` |

## 10. Verification Notes

All API examples in this document must be checked against the running application before final submission.

The request and response examples that contain illustrative values must be replaced or supplemented with actual outputs captured from the current database.

The API documentation describes the current implementation and does not claim that authentication, role-based authorization, or production deployment has been completed.