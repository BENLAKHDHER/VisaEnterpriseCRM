from fastapi import FastAPI

app = FastAPI(
    title="Visa Enterprise CRM",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "Visa Enterprise CRM",
        "version": "1.0.0",
        "status": "running"
    }