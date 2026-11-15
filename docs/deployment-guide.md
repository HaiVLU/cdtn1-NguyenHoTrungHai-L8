
# DEPLOYMENT GUIDE
## Smart CRM – Mekong Mobile (L8)

## 1. System Requirements

| Component | Requirement |
|---|---|
| Operating System | Windows 10/11, Linux or macOS |
| Docker | Docker Desktop with Docker Compose |
| Python | Not required on the host when using Docker |
| Node.js | Not required on the host when using Docker |
| PostgreSQL | Runs inside Docker |
| Memory | At least 4 GB RAM recommended |
| Backend Port | 5000 |
| Frontend Port | 5173 |
| Database Port | Internal Docker network |

The application uses three services:

- PostgreSQL 16: Database service.
- Flask: Backend REST API.
- React with Vite: Frontend application.

## 2. Deployment Steps

### Step 1 – Clone the repository

```bash
git clone https://github.com/HaiVLU/cdtn1-NguyenHoTrungHai-L8.git
cd cdtn1-NguyenHoTrungHai-L8
```

For the submission version, use the v1.0 tag:

```bash
git checkout v1.0
```

### Step 2 – Configure environment variables

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

On Linux or macOS:

```bash
cp .env.example .env
```

The example configuration is intended for local academic testing.

### Step 3 – Build and start the application

```bash
docker compose up -d --build
```

Docker Compose starts the database, backend and frontend services.

The Backend automatically performs database migration and executes the sample data script.

### Step 4 – Verify service status

```bash
docker compose ps
```

Expected result:

- l8-postgres: healthy
- l8-backend: healthy
- l8-frontend: healthy

## 3. Environment Variables

| Variable | Description | Required | Example |
|---|---|---|---|
| SECRET_KEY | Flask application secret key | Yes | local-development-secret |
| POSTGRES_DB | PostgreSQL database name | Yes | l8_csat_nps |
| POSTGRES_USER | PostgreSQL username | Yes | l8_user |
| POSTGRES_PASSWORD | PostgreSQL password | Yes | l8_local_password |
| DATABASE_URL | Local development database connection | Outside Docker | postgresql+psycopg://l8_user:l8_local_password@localhost:5432/l8_csat_nps |

Inside Docker, the Backend uses the database hostname `db`.

Do not commit the actual `.env` file or production credentials.

## 4. Sample Data

The project uses:

- `migrations/`: Database schema migration.
- `seed.py`: Sample data initialization.

The startup command runs:

```bash
flask --app run:app db upgrade
python seed.py
```

The current seed script creates sample records for:

- Service centers
- Technicians
- Customers
- Date dimension
- Closed warranty tickets
- Survey responses

The seed script checks whether a service center already exists before inserting the sample dataset.

Record counts must be verified from the actual database after deployment.

To execute the seed script manually:

```bash
docker compose exec backend python seed.py
```

Run the command a second time and verify that no duplicate sample dataset is created.

## 5. System Verification

### 5.1. Check Backend Health

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

### 5.2. Check Survey API

```powershell
Invoke-RestMethod http://localhost:5000/api/surveys
```

Expected result:

- HTTP 200
- JSON response
- Survey data returned when sample records exist.

### 5.3. Check Frontend

Open:

http://localhost:5173

Expected result:

The Smart CRM login page is displayed.

### 5.4. Run Automated Tests

```bash
docker compose exec backend python -m pytest -o pythonpath=. -v
```

Expected result:

All collected tests pass.

Record the actual number of passed and failed tests.

### 5.5. Inspect Application Logs

```bash
docker compose logs --tail=100
```

Expected result:

No startup, migration or database connection errors.

## 6. Stop the Application

```bash
docker compose down
```

To remove the database volume as well:

```bash
docker compose down -v
```

Warning: The second command permanently removes the Docker database volume and its stored records.
