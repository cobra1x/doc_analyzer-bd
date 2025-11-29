from app.api.routes import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=[
  "https://ai-legalmate.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
