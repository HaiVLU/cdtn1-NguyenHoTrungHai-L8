
# TEST PLAN – SMART CRM MEKONG MOBILE (L8)

## 1. Test Scope

### 1.1. In Scope

The testing covers the implemented CSAT/NPS survey validation logic.

- Validate JSON object structure.
- Validate required survey fields.
- Validate integer data types.
- Validate positive ticket_id and date_id.
- Validate CSAT score from 1 to 5.
- Validate NPS survey score from 0 to 10.
- Validate optional comment.
- Verify QT-10: the warranty ticket must exist and be closed.
- Verify that the survey date exists.
- Prevent duplicate survey responses for the same ticket.
- Verify that updating the current survey does not trigger a duplicate error.
- Verify deterministic validation results.

### 1.2. Out of Scope

The following tests are not implemented in the current test suite:

- Real PostgreSQL integration tests.
- Complete API integration tests.
- Frontend browser tests.
- Backend authentication and authorization tests.
- Service-center ownership access control.
- Performance and load testing.
- Penetration testing.

These areas are excluded because the current automated suite focuses on service-layer validation and uses mocked repository methods.

## 2. Test Types and Quantities

| Test Type | Quantity | Implementation |
|---|---:|---|
| Unit Testing | 38 expected cases | pytest |
| Integration Testing | 0 | Not implemented |
| API Testing | 0 | Not implemented |
| End-to-End Testing | 0 | Not implemented |
| Total | 38 expected cases | Verify during execution |

The test suite uses parameterized test scenarios.

The Test Report contains 12 representative test cases.

## 3. Measurable Success Criteria

- All collected unit test cases must PASS.
- Required fields must be validated.
- CSAT scores must be within 1–5.
- NPS survey scores must be within 0–10.
- QT-10 must reject missing or unclosed warranty tickets.
- Duplicate survey responses must be rejected.
- Identical input must produce identical validation results.
- No unresolved Critical bug may remain.

Actual results must be recorded after execution.

## 4. Test Environment and Test Data

| Item | Configuration |
|---|---|
| Operating System | Windows 10/11 |
| Python | 3.13.x |
| Framework | Flask |
| Test Framework | pytest |
| Database | PostgreSQL 16 for application runtime |
| Test Database | Not used by current unit tests |
| Test File | tests/test_survey_validation.py |
| Test Data | Deterministic data defined in test file |
| Repository | Mocked repository methods |

Test execution:

python -m pytest -o pythonpath=. -v

## 5. Test Execution Criteria

Testing is successful when:

- All collected test cases pass.
- No test collection error occurs.
- The execution result is repeatable.
- Actual PASS/FAIL results and execution time are recorded.

## 6. Known Testing Limitations

The current suite does not verify:

- Real PostgreSQL transactions.
- All REST API responses.
- Authentication and authorization.
- Frontend user interactions.
- Service-center ownership restrictions.

These limitations must not be interpreted as completed testing.
