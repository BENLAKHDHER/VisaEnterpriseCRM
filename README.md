# VisaEnterpriseCRM

> CRM de gestion des dossiers Visa développé avec FastAPI, PostgreSQL et JWT Authentication.

---

## 🚧 Statut du projet

Version actuelle : MVP Backend v1

### Fonctionnalités terminées

✅ Architecture Backend

✅ PostgreSQL Integration

✅ SQLAlchemy ORM

✅ CRUD Clients complet

✅ Gestion des utilisateurs

✅ Hashage sécurisé des mots de passe

✅ JWT Authentication

✅ Routes protégées

✅ Endpoint GET /me

### Fonctionnalités en cours

🔄 Roles & Permissions

🔄 Visa Applications Module

### Fonctionnalités prévues

⏳ Dashboard

⏳ Reports

⏳ Notifications

⏳ Frontend React

⏳ Docker Deployment

---

# 📦 Stack Technique

## Backend

- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Database

- PostgreSQL 18.7.1

## Security

- JWT Authentication
- BCrypt
- Passlib
- python-jose

## Development

- Python 3.15.2
- Git
- GitHub
- VS Code

---

# 🏗️ Architecture

```text
Frontend
    ↓
FastAPI
    ↓
API Routes
    ↓
Pydantic Schemas
    ↓
Repositories
    ↓
SQLAlchemy ORM
    ↓
PostgreSQL
```

---

# 📁 Project Structure

```text
VisaEnterpriseCRM
│
├── README.md
│
├── backend
│   │
│   ├── requirements.txt
│   ├── tests
│   ├── venv
│   │
│   └── app
│       │
│       ├── api
│       │   ├── auth_routes.py
│       │   ├── client_routes.py
│       │   └── user_routes.py
│       │
│       ├── models
│       │   ├── client.py
│       │   └── user.py
│       │
│       ├── schemas
│       │   ├── client_schema.py
│       │   └── user_schema.py
│       │
│       ├── repositories
│       │   ├── client_repository.py
│       │   └── user_repository.py
│       │
│       ├── database
│       │   ├── connection.py
│       │   ├── base.py
│       │   ├── create_tables.py
│       │   └── test_connection.py
│       │
│       ├── core
│       │   ├── security.py
│       │   └── auth_dependency.py
│       │
│       └── main.py
│
├── docs
│
├── frontend
│
├── database
│
├── docker
│
└── prompts
```

---

# 🗄️ Database

## Database

```text
visa_crm
```

## Application User

```text
visa_crm_user
```

## Existing Tables

### clients

```text
id
first_name
last_name
email
phone
passport_number
```

### users

```text
id
username
email
password_hash
is_active
```

---

# 🔐 Security

Implemented security features:

- Password hashing with BCrypt
- JWT Authentication
- Bearer Token Authorization
- Protected Routes
- Current User Endpoint

Authentication flow:

```text
User
↓
Login
↓
JWT Token
↓
Protected API
```

---

# 🚀 Implemented Endpoints

## System

```http
GET /
```

---

## Authentication

```http
GET /auth
```

```http
POST /auth/login
```

```http
GET /me
```

---

## Users

```http
POST /users
```

---

## Clients

```http
POST /clients
```

```http
GET /clients
```

```http
GET /clients/{id}
```

```http
PUT /clients/{id}
```

```http
DELETE /clients/{id}
```

---

# 🎯 Next Milestones

## Security Layer

- Roles
- Permissions
- Authorization Policies

## Business Layer

- Visa Applications
- Visa Status Tracking
- Document Management
- Appointment Management

## Dashboard

- KPIs
- Statistics
- Reporting

## Frontend

- React
- Authentication UI
- Dashboard UI
- Client Management UI

---

# 👨‍💻 Author

GitHub:

**BENLAKHDHER**

Project:

**VisaEnterpriseCRM**