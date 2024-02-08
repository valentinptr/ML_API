from fastapi import FastAPI

from ml import models
from ml.database import engine
from ml.routers import ml, authentication, users


app = FastAPI(
    title="ML Fast API",
    description="API for interact with Rock, Paper, Scissors AI model.",
    version="0.0.1",
    contact={
        "name": "Valentin ",
        "email": "valentin@example.com",
    },
    license_info={
        "name": "licence",
    },
)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(ml.router)
