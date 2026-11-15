
# DEPLOYMENT GUIDE
## Smart CRM – Mekong Mobile (L8)

## 1. System Requirements

| Component | Requirement |
|---|---|
| Operating System | Windows 10/11, Linux or macOS |
| Docker | Docker Desktop with Docker Compose |
| Memory | 4 GB RAM minimum recommended |
| Disk Space | Sufficient space for Docker images and database |
| Frontend Port | 8080 |
| Backend Port | 5000 |
| Database Port | Internal Docker network |

No local Python, Node.js or PostgreSQL installation is required when using Docker Compose.

## 2. Deployment Steps

### Step 1 – Configure Environment

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

Update the environment variables using local values.

### Step 2 – Build and Start Services

```powershell
docker compose up -d --build
```

### Step 3 – Check Service Status

```powershell
docker compose ps
```

All required services must report a healthy status.

## 3. Environment Variables

| Variable | Description | Required |
|---|---|---|
| SECRET_KEY | Flask application secret | Yes |
| DATABASE_URL | PostgreSQL connection string | Yes |

Actual example values must match the committed `.env.example`.

## 4. Sample Data

The application uses the project's existing database migration and seed process.

Seed script:

`seed.py`

Sample records are created using the existing project data definitions.

The seed process must be tested twice to verify that duplicate records are not created.

Actual record counts must be recorded after deployment.

## 5. System Verification

### Backend Health Check

```powershell
Invoke-RestMethod http://localhost:5000/health
```

Expected response:

```json
{
  "status": "ok",
  "message": "L8 API is running"
}
```

### Survey API

```powershell
Invoke-RestMethod http://localhost:5000/api/surveys
```

Expected result: HTTP 200 and a JSON response.

### Frontend

Open:

`http://localhost:8080`

Expected result: The Smart CRM login page is displayed.

### Automated Tests

```powershell
docker compose exec backend python -m pytest -o pythonpath=. -v
```

Expected result: All collected tests pass.

Actual deployment results and screenshots must be recorded before submission.
