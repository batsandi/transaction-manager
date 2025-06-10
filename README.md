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

## High-Level Technical Design
__Core Technologies & Principles__

The application is built on a modern, decoupled architecture designed for maintainability and a clear separation of concerns.

__Backend Framework__: FastAPI 

__Frontend Framework__: Vue 3 (JavaScript)

__Database__: PostgreSQL 

__Data Modeling__: SQLModel

__Containerization__: Docker Compose 

__Backend Architecture__

__API Layer__: The public-facing interface that defines all endpoints, validates requests, and shapes responses.

__Security & Authentication Layer__: Handles user credential verification, JWT generation and validation, and endpoint protection.

__Business Logic & CRUD Layer__: Contains the core application logic and data manipulation functions (Create, Read, Update, Delete).

__Database Interface Layer:__ Manages all direct interaction with the PostgreSQL database, providing reliable sessions for executing queries.

__Frontend Architecture__


__Component & View Layer__: The visual part of the application, composed of larger "Views" (pages) and smaller, reusable "Components" (UI elements).

__Routing Service (Vue Router)__: Manages all client-side navigation, mapping URLs to Views and protecting authenticated routes.

__State Management Service (Pinia)__: A centralized store for global application state, primarily the user's authentication status and token.

__API Service (Axios)__: A dedicated module that handles all communication with the backend API, automatically attaching authentication headers to requests.