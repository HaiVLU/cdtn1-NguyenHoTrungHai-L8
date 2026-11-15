
# TEST REPORT – SMART CRM MEKONG MOBILE (L8)

## 1. Test Information

- Project: Smart CRM – Mekong Mobile
- Module: CSAT/NPS Survey
- Track: Software Engineering (SE)
- Framework: pytest
- Test File: tests/test_survey_validation.py
- Test Plan: test-plan.md

## 2. Test Case Results

| ID | Preconditions | Test Steps | Test Data | Expected Result | Priority | Actual Result | Status |
|---|---|---|---|---|---|---|---|
| TC01 | Validation service available | Submit valid survey data | ticket_id=1001, date_id=20261001, score=5, nps_score=10 | Data accepted | High | Pending execution | PENDING |
| TC02 | Validation service available | Submit survey without comment and with null comment | comment omitted / null | Data accepted | Medium | Pending execution | PENDING |
| TC03 | Validation service available | Test minimum and maximum CSAT values | score=1 and score=5 | Both values accepted | High | Pending execution | PENDING |
| TC04 | Validation service available | Test minimum and maximum NPS values | nps_score=0 and nps_score=10 | Both values accepted | High | Pending execution | PENDING |
| TC05 | Validation service available | Submit invalid request body types | null, list, string, integer | ValidationError returned | High | Pending execution | PENDING |
| TC06 | Validation service available | Remove required fields | ticket_id, date_id, score, nps_score | Missing field rejected | High | Pending execution | PENDING |
| TC07 | Validation service available | Submit incorrect data types and invalid IDs | String IDs, boolean score, zero/negative ID | ValidationError returned | High | Pending execution | PENDING |
| TC08 | Validation service available | Submit scores outside allowed ranges | CSAT=0,6; NPS=-1,11 | Invalid values rejected | High | Pending execution | PENDING |
| TC09 | Business rule mocks configured | Submit survey for missing or unclosed ticket | Ticket missing / OPEN / PENDING / IN_PROGRESS | Survey rejected | High | Pending execution | PENDING |
| TC10 | Business rule mocks configured | Submit survey with missing date | date_id not found | Survey rejected | High | Pending execution | PENDING |
| TC11 | Existing survey configured | Submit duplicate survey and update current survey | Existing response_id=77 | Duplicate rejected; current record update validation accepted | High | Pending execution | PENDING |
| TC12 | Validation service available | Run identical validation twice | Same valid survey data | Both results identical | Medium | Pending execution | PENDING |

## 3. Test Execution Summary

- Expected collected test cases: 38
- Actual executed test cases: Pending
- PASS: Pending
- FAIL: Pending
- Execution time: Pending

## 4. Testing Categories

| Category | Covered |
|---|---|
| Positive Testing | Yes |
| Boundary Testing | Yes |
| Negative Testing | Yes |
| Data Quality Testing | Yes |
| Reproducibility Testing | Yes |

## 5. Testing Limitations

- Current tests focus on service-layer validation.
- Business rules use mocked repository methods.
- Full PostgreSQL integration testing has not been implemented.
- Complete API and frontend testing have not been implemented.
- Authentication and authorization testing remain outstanding.

## 6. Evidence

Actual pytest terminal screenshots must be stored in:

`docs/screenshots/`

Do not report PASS without an actual successful execution.

## 7. Continuous Integration

GitHub Actions workflow:

`.github/workflows/python-tests.yml`

CI status must be updated after checking the actual GitHub Actions execution.
