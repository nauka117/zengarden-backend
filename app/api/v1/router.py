from fastapi import APIRouter
from app.api.v1.endpoints import auth, flowers

api_router = APIRouter()

# Auth endpoints are available at /auth/register and /auth/token
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# Flower endpoints are available at /flowers/*
api_router.include_router(flowers.router, prefix="/flowers", tags=["flowers"]) 