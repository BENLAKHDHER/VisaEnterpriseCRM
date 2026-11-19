Architecture Technique
Vision
Application CRM Visa Enterprise

Architecture :

Frontend ↓ FastAPI ↓ Services ↓ Repositories ↓ PostgreSQL

Structure du projet
VisaEnterpriseCRM

├── backend ├── frontend ├── docs ├── database ├── docker └── prompts

Backend
backend

├── app │ ├── api │ ├── models │ ├── schemas │ ├── services │ ├── repositories │ ├── database │ ├── core │ └── main.py

Responsabilités
api

Routes FastAPI

models

Modèles SQLAlchemy

schemas

Validation Pydantic

services

Logique métier

repositories

Accès base de données

database

Connexion PostgreSQL

core

Configuration globale Sécurité JWT Variables d'environnement

main.py

Point d'entrée FastAPI