# Transaction Manager

This project is a full-stack Single-Page Application for managing financial transactions, built with FastAPI, Vue.js, and PostgreSQL, all orchestrated with Docker.

## Prerequisites

- Git
- Docker & Docker Compose

## Run Locally

Clone the repo locally

```
git clone git@github.com:batsandi/transaction-manager.git
```

Navigate to directory

```
cd transaction-manager
```

create a `.env` file in the project root with the following content.

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=transactions_db
DATABASE_URL="postgresql://admin:mysecretpassword@db:5432/transactions_db"
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
```

Build the project

```
docker compose -f docker-compose.dev.yaml up --build
```

Access the app at http://localhost:5173

shut down with

```
docker compose down -v
```
