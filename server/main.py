from fastapi import FastAPI
from routes.query import router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/sql-agent")

