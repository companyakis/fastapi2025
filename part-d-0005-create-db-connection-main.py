from fastapi import FastAPI

from database import engine
import models

app = FastAPI()

# remember => ALCHEMY_DB_URL = 'sqlite:///./todoapp.db'

models.Base.metadata.create_all(bind=engine)
