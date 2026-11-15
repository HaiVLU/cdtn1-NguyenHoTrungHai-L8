
# SECURITY CHECKLIST
## Smart CRM – Mekong Mobile

| No. | Security Requirement | Status | Evidence / Notes |
|---|---|---|---|
| 1 | No secrets committed to the repository | CHƯA LÀM | `.env.example` contains placeholders. Git history must still be checked for previously committed secrets. |
| 2 | Input validation at application level | ĐÃ LÀM | `src/services/survey_service.py` and `src/services/service_center_service.py` validate input data. Validation coverage is limited to implemented fields. |
| 3 | Access control based on data ownership | CHƯA LÀM | Report routes do not currently enforce authenticated user or service-center ownership. |
| 4 | Passwords and sensitive data are hashed or encrypted | CHƯA LÀM | Admin credentials are currently hardcoded in `frontend/src/App.jsx`; no secure backend password storage is implemented. |
| 5 | Error messages do not expose internal information | CHƯA LÀM | `src/routes/report_routes.py` returns a generic error response, but global error handling and debug configuration require further verification. |
| 6 | Logs do not expose secrets or unnecessary personal data | CHƯA LÀM | Logging behavior requires further verification against actual application logs. |
| 7 | Dependencies are pinned and basic vulnerability checks are performed | CHƯA LÀM | Python dependencies are pinned in `requirements.txt`. Frontend lockfile exists; vulnerability scan evidence is not yet available. |

## Security Assessment

The current prototype implements basic application-level input validation.

Authentication, authorization, password protection and comprehensive security verification remain limitations.

The prototype must not be considered production-ready until these issues are addressed.
