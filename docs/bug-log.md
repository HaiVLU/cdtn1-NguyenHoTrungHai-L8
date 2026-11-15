
# BUG LOG – SMART CRM MEKONG MOBILE (L8)

## BUG-01 – Frontend Port Mismatch

- Severity: [Major / Minor - confirm after reproduction]
- Status: [Fixed only after verification]
- Module: Deployment Configuration
- Detected by: Deployment verification test

### 1. Preconditions
The project is configured using Docker Compose.

### 2. Reproduction Steps
1. Inspect the Frontend port mapping in docker-compose.yml.
2. Inspect the Frontend URL in docs/deployment-guide.md.
3. Compare both configurations.

### 3. Expected Result
The Deployment Guide must use the actual exposed Frontend port.

### 4. Actual Result
The original guide specified port 8080, while Docker Compose exposed port 5173.

### 5. Root Cause
The Frontend port configuration was changed or updated without synchronizing the Deployment Guide.

### 6. Fix
- File: docs/deployment-guide.md
- Change: Updated the documented Frontend URL to port 5173.
- Verification: [Record actual verification result]

### 7. Regression Test
- Test Case: [Actual test case ID]
- Result: [PASS/FAIL after execution]

### 8. Commit
[Insert actual GitHub commit URL]

---

## BUG-02 – Sample Data Not Loaded Automatically

- Severity: [Major / Minor - confirm after reproduction]
- Status: [Fixed only after verification]
- Module: Docker Deployment
- Detected by: Clean deployment test

### 1. Preconditions
A new PostgreSQL volume is used.

### 2. Reproduction Steps
1. Start the application using the original Docker Compose configuration.
2. Inspect the PostgreSQL tables.
3. Check whether sample records are available.

### 3. Expected Result
Sample data must be available after following the Deployment Guide.

### 4. Actual Result
The original Backend startup command ran database migrations but did not execute seed.py.

### 5. Root Cause
The seed script was not included in the Docker startup command.

### 6. Fix
- File: docker-compose.yml
- Change: Added python seed.py after successful migration.
- Verification: [Record actual verification result]

### 7. Regression Test
- Test Case: [Actual test case ID]
- Result: [PASS/FAIL after execution]

### 8. Commit
[Insert actual GitHub commit URL]

---

## BUG-03 – Missing Application Health Checks

- Severity: [Major / Minor - confirm after reproduction]
- Status: [Fixed only after verification]
- Module: Docker Compose
- Detected by: Deployment verification test

### 1. Preconditions
The application is started using Docker Compose.

### 2. Reproduction Steps
1. Inspect the Backend service configuration.
2. Inspect the Frontend service configuration.
3. Run docker compose ps.

### 3. Expected Result
Backend and Frontend must provide health checks so that their service readiness can be verified.

### 4. Actual Result
The original configuration only defined a PostgreSQL health check.

### 5. Root Cause
Health checks were configured for the database but not for the application services.

### 6. Fix
- File: docker-compose.yml
- Change: Added HTTP health checks for Backend and Frontend.
- Verification: [Record actual verification result]

### 7. Regression Test
- Test Case: [Actual test case ID]
- Result: [PASS/FAIL after execution]

### 8. Commit
[Insert actual GitHub commit URL]

---

## Bug Verification Notes

Only bugs that have been reproduced, fixed and verified may be marked as Fixed.

All commit URLs must point to the actual commits containing the corresponding fixes.
