from fastapi import FastAPI

from app.api.client_routes import router as client_router

from app.api.user_routes import router as user_router

from app.api.auth_routes import router as auth_router


app = FastAPI(
    title="Visa Enterprise CRM",
    version="1.0.0"
)


app.include_router(client_router)

app.include_router(user_router)


@app.get("/")
def home():
    return {
        "application": "Visa Enterprise CRM",
        "version": "1.0.0",
        "status": "running"
    }

app.include_router(auth_router)