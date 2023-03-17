from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from .db import db
from typing import List
from .models import User, Exercise, Workout, Program
from .utils import API


app = FastAPI()

api = API()


@app.get("/users", response_model=List[User])
async def read_users():
    return await api.get_users()


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    return await api.get_user(user_id)


@app.post("/users", response_model=User)
async def create_new_user(user: User):
    return await api.create_user(user)


@app.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: str, user: User):
    return await api.update_user(user_id, user)


@app.delete("/users/{user_id}")
async def remove_user(user_id: str):
    return await api.delete_user(user_id)
