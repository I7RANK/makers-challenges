from fastapi import FastAPI
from app.routes import challenge_e9
from app.routes import challenge_e7 

app = FastAPI(
  title="Backend Challenges API",
  description="Solutions to technical challenges using FastAPI",
  version="1.0.0"
)

app.include_router(challenge_e9.router)
app.include_router(challenge_e7.router)