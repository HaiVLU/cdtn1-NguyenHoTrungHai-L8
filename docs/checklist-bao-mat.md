
# SECURITY CHECKLIST
## Smart CRM – Mekong Mobile (L8)

| No. | Security Requirement | Status | Evidence |
|---|---|---|---|
| 1 | No secrets committed to the repository | CHƯA LÀM | `.env.example` contains sample values. Git history still needs a complete secret scan. |
| 2 | Application-level input validation | ĐÃ LÀM | `src/services/survey_service.py` validates required fields, data types, CSAT/NPS ranges and QT-10 business rules. |
| 3 | Access control based on data ownership | CHƯA LÀM | Backend routes currently do not enforce authenticated user identity or service-center ownership. |
| 4 | Passwords and sensitive information are hashed or encrypted | CHƯA LÀM | The current admin login uses frontend-side credential comparison. No secure backend password storage is implemented. |
| 5 | Error messages do not expose internal implementation details | CHƯA LÀM | Report routes have error handling, but all API error paths and production debug configuration have not been verified. |
| 6 | Logs do not expose secrets or unnecessary personal data | CHƯA LÀM | Application logging has not been fully audited using actual runtime logs. |
| 7 | Dependencies are pinned and basic vulnerability checks are performed | CHƯA LÀM | Python dependencies are pinned. Frontend lockfile exists. Vulnerability scan results have not yet been recorded. |

## Security Assessment

The prototype currently implements basic input validation.

The following security controls are not fully implemented:

- Backend authentication.
- Authorization based on service-center ownership.
- Secure password hashing and storage.
- Complete error response verification.
- Full logging audit.
- Dependency vulnerability assessment.

The prototype is intended for academic demonstration and must not be considered production-ready.

## Verification Evidence

The following evidence must be collected before submission:

1. Git history secret scan.
2. Input validation test results.
3. Backend ownership authorization test.
4. Password storage inspection.
5. API error response inspection.
6. Runtime log inspection.
7. Dependency vulnerability scan report.
