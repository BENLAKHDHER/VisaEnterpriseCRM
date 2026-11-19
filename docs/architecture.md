Architecture Technique
Vision
CRM Visa Enterprise

Architecture générale :

Frontend ↓ FastAPI ↓ Services ↓ Repositories ↓ PostgreSQL

Structure du projet
VisaEnterpriseCRM

├── backend ├── frontend ├── docs ├── database ├── docker └── prompts

Backend
backend

├── app │ ├── api ├── models ├── schemas ├── services ├── repositories ├── core ├── database │ └── main.py

Responsabilités
api

Routes HTTP

models

Modèles SQLAlchemy

schemas

Validation Pydantic

services

Logique métier

repositories

Accès aux données

database

Connexion PostgreSQL

core

Configuration JWT Sécurité Variables d'environnement

main.py

Point d'entrée FastAPI