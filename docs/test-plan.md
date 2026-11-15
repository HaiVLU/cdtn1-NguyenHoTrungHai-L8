
# TEST PLAN – SMART CRM MEKONG MOBILE (L8)

## 1. Test Scope

### 1.1. In Scope

The testing focuses on the survey validation and business rules implemented in the Backend.

- Validate survey request data using `validate(data)`.
- Check required fields and data types.
- Check CSAT score range from 1 to 5.
- Check NPS survey score range from 0 to 10.
- Verify QT-10: a warranty ticket must exist and be closed before accepting a survey.
- Verify the survey date exists.
- Prevent duplicate survey responses for the same warranty ticket.
- Verify that updating the current survey does not trigger a duplicate error.
- Verify repeatable validation results.

### 1.2. Out of Scope

- Full PostgreSQL integration testing.
- Complete CRUD API testing.
- React UI and browser compatibility testing.
- Authentication and authorization testing.
- Performance and load testing.
- Penetration testing.

These areas are excluded because the current automated test suite focuses on service-layer validation and uses mocked repositories.

## 2. Test Types and Quantities

| Test Type | Quantity | Description |
|---|---:|---|
| Unit Test | 38 expected pytest cases | Survey validation and business rules |
| Integration Test | 0 | Not implemented |
| API Test | 0 | Not implemented |
| End-to-End Test | 0 | Not implemented |
| Total | 38 expected cases | Subject to execution verification |

The 38 cases include parameterized test scenarios.

The Test Report presents 12 representative test scenarios covering the five required testing categories.

## 3. Measurable Success Criteria

- All 38 collected pytest cases must PASS.
- All required survey fields must be validated.
- CSAT values must remain within 1–5.
- NPS survey scores must remain within 0–10.
- QT-10 business rules must be enforced.
- Duplicate survey responses must be rejected.
- Repeated validation with identical input must produce identical results.
- No unresolved Critical bug may remain.

The test results must be recorded from an actual execution.

## 4. Test Environment and Test Data

| Item | Configuration |
|---|---|
| Operating System | Windows |
| Python | 3.13.5 |
| Testing Framework | pytest 9.2.0 |
| Backend | Flask |
| Database | PostgreSQL is used by the application; unit tests do not access the real database |
| Test File | `tests/test_survey_validation.py` |
| Test Data | Deterministic data defined in the test file |
| Repository Mocking | Mock repository methods |
| Test Execution | `python -m pytest -o pythonpath=. -v` |

The current unit tests do not insert or delete records in PostgreSQL. Repository methods are mocked to isolate the service-layer validation logic.

## 5. Test Execution Criteria

Testing is considered successful when all collected test cases pass without collection errors.

Actual PASS/FAIL results and execution time must be recorded in the Test Report.
