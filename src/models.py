from typing import List
from datetime import datetime
from pydantic import BaseModel, Field

# Models


class User(BaseModel):
    id: str = Field(alias="_id")
    username: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime


class Exercise(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: str
    difficulty: str
    category: str
    media_url: str


class Workout(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: str
    exercises: List[Exercise]
    duration: int
    difficulty: str


class Program(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: str
    workouts: List[Workout]
    duration: int
    difficulty: str
    creator: User
