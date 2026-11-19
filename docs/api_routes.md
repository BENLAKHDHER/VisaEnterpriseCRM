API Routes
État actuel
Application opérationnelle

Routes existantes
GET /

Réponse :

{ "application": "Visa Enterprise CRM", "version": "1.0.0", "status": "running" }

Routes prévues
Authentification
POST /auth/login

POST /auth/refresh

POST /auth/logout

Clients
GET /clients

GET /clients/{id}

POST /clients

PUT /clients/{id}

DELETE /clients/{id}

Visa Applications
GET /visa-applications

GET /visa-applications/{id}

POST /visa-applications

PUT /visa-applications/{id}

DELETE /visa-applications/{id}

Dashboard
GET /dashboard