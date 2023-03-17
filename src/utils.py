from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime
from .db import db
from .models import User


class API:
    async def get_users(self):
        users = []
        async for user in db.users.find():
            users.append(User(**user))
        return users

    async def get_user(self, user_id: str):
        user = await db.users.find_one({"_id": user_id})
        if user:
            return User(**user)
        else:
            raise HTTPException(status_code=404, detail="User not found")

    async def create_user(self, user: User):
        new_user = await db.users.insert_one(user.dict(by_alias=True))
        created_user = await db.users.find_one({"_id": new_user.inserted_id})
        return User(**created_user)

    async def update_user(self, user_id: str, user: User):
        result = await db.users.replace_one({"_id": user_id}, user.dict(by_alias=True))
        if result.modified_count == 1:
            return User(**user.dict(by_alias=True))
        else:
            raise HTTPException(status_code=404, detail="User not found")

    async def delete_user(self, user_id: str):
        result = await db.users.delete_one({"_id": user_id})
        if result.deleted_count == 1:
            return {"result": "User deleted"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
