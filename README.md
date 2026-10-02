# Data Platform Core

A production-style Data & AI Platform Engineering portfolio, built week by week over 24 weeks.

This repository documents my journey from Python fundamentals to a full cloud-native data platform: FastAPI ingestion, Airflow-orchestrated pipelines, dbt transformations, a Kubernetes-deployed multi-tenant LLM gateway, and Terraform-provisioned AWS infrastructure.

## Project Status

| Phase | Weeks | Focus | Status |
| --- | --- | --- | --- |
| 1 | 01-04 | Foundation: Python, Git, PostgreSQL, FastAPI | 🟡 In Progress |
| 2 | 05-10 | Batch ingestion, Parquet, Airflow, dbt | ⚪ Not Started |
| 3 | 11-16 | CI, LLM gateway, Kubernetes, observability | ⚪ Not Started |
| 4 | 17-20 | Terraform, AWS, automated deployments | ⚪ Not Started |
| 5 | 21-24 | Polish, positioning, outreach, interviews | ⚪ Not Started |

## Repository Structure

```text
data-platform-core/
├── .env.example                              # Template for environment variables
├── .gitignore                                # Excludes secrets, venv, and cache files
├── README.md                                 # Project documentation
├── config.py                                 # Loads environment variables via os.getenv()
├── requirements.txt                          # Python dependencies
├── src/
│   └── utils.py                              # Shared helper functions
├── week-01-python-foundations/
│   ├── README.md
│   ├── strings.py
│   ├── integers_floats.py
│   ├── list_tuples_sets.py
│   ├── dictionaries.py
│   ├── conditionals.py
│   ├── loops-and-iterations.py
│   ├── functions.py
│   └── main.py                               # FastAPI app with /health and /data
├── week-02-git-virtual_environments-repo_setup/
│   └── venv.py                               # Notes on virtual environments
└── week-03-postgresql/                       # Coming soon
```

## Tech Stack

| Layer | Tools |
| --- | --- |
| Language | Python 3.11+ |
| API | FastAPI, Uvicorn, Pydantic |
| Database | PostgreSQL, SQLAlchemy, psycopg2 |
| Orchestration | Apache Airflow, dbt |
| Storage | MinIO (S3-compatible), Parquet, PyArrow |
| Containers | Docker, Docker Compose, Kubernetes (Minikube), Helm |
| Observability | Prometheus, Grafana |
| Cloud | AWS (EC2, RDS, S3, IAM), Terraform |
| CI/CD | GitHub Actions |
| Version Control | Git, GitHub |

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Somesh-Tiwari/data-platform-core.git
cd data-platform-core
```

### 2. Create and activate a virtual environment

**Windows (Git Bash):**

```bash
python -m venv env
source env/Scripts/activate
```

**Windows (CMD):**

```bat
python -m venv env
env\Scripts\activate
```

**macOS / Linux:**

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file at the root of the project:

```bash
cp .env.example .env
```

Then edit `.env` with your own values:

```dotenv
OPENAI_API_KEY=your-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

> **Important:** `.env` is listed in `.gitignore` and should never be committed. Never hardcode secrets in source files.

### 5. Verify the setup

```bash
python config.py
```

You should see your environment variables printed to the console.

## Running the FastAPI App

From the `week-01-python-foundations/` folder:

```bash
uvicorn main:app --reload
```

Available endpoints:

- [`/health`](http://127.0.0.1:8000/health) - `{"status": "healthy"}`
- [`/data`](http://127.0.0.1:8000/data) - Sample data
- [`/docs`](http://127.0.0.1:8000/docs) - Auto-generated API docs

## Daily Ritual

Every coding session follows the same rhythm:

- Activate the environment: `source env/Scripts/activate`
- Lock dependencies: `pip freeze > requirements.txt`
- Check for secrets: `git status` and confirm `.env` is not staged
- Save progress: `git add . && git commit -m "feat: ..." && git push`
- Sweep workloads: `docker ps` and `kubectl get pods`

## Roadmap

This project follows a structured 24-week curriculum covering:

- Week 01: Python core syntax + FastAPI
- Week 02: Git, virtual environments, repo setup
- Week 03: PostgreSQL, window functions, CTEs
- Week 04: FastAPI ingestion, Pydantic validation, Postgres persistence
- Week 05: Error handling, logging, batch ingestion
- Week 06: Pandas + PyArrow, Parquet to MinIO
- Week 07: Docker Compose (Postgres, MinIO, Adminer)
- Week 08: Load Parquet from MinIO into Postgres
- Week 09: Airflow hourly ingestion DAG
- Week 10: dbt - raw to clean customers
- Week 11: GitHub Actions - dbt tests + Slack alerts
- Week 12: OpenAI API + JSON enforcement, K8s-ready container
- Week 13: Multi-tenant logging + Redis cache
- Week 14: Retries + Minikube deployment
- Week 15: Load testing + Prometheus & Grafana
- Week 16: Advanced SQL prep + Helm charts
- Week 17: Terraform - AWS EC2 + RDS Postgres
- Week 18: Terraform - S3 + IAM
- Week 19: dbt certification + Terraform in CI
- Week 20: Cold outreach - startup CTOs
- Week 21: README polish + walkthrough video
- Week 22: LinkedIn overhaul
- Week 23: Cold outreach intensive
- Week 24: System design interview prep

## Author

**Somesh Tiwari**  
Aspiring Data & AI Platform Engineer

[GitHub: @Somesh-Tiwari](https://github.com/Somesh-Tiwari)

## License

This project is for personal learning and portfolio purposes.
