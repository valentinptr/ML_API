from fastapi import FastAPI

from app.ml import models
from app.ml.database import engine
from app.ml.routers import ml, authentication


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(ml.router)
