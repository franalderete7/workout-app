from typing import List
from fastapi import FastAPI, HTTPException
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from pydantic import BaseModel

app = FastAPI()

# MongoDB connection

client = MongoClient('mongodb://localhost:27017/')
db = client['workout_app']

# Models


class User(BaseModel):
    id: str
    username: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime


class Exercise(BaseModel):
    id: str
    name: str
    description: str
    difficulty: str
    category: str
    media_url: str


class Workout(BaseModel):
    id: str
    name: str
    description: str
    exercises: List[Exercise]
    duration: int
    difficulty: str


class Program(BaseModel):
    id: str
    name: str
    description: str
    workouts: List[Workout]
    duration: int
    difficulty: str
    creator: User

# Helper Functions


def document_to_model(doc: dict, model: BaseModel) -> BaseModel:
    return model(**doc)

# Routes


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def get_users():
    users = []
    for doc in db.users.find():
        user = document_to_model(doc, User)
        users.append(user.dict())
    return users


@app.post("/users")
def create_user(user: User):
    doc = user.dict()
    result = db.users.insert_one(doc)
    if result.acknowledged:
        return {"message": "User created", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create user")


@app.get("/exercises")
def get_exercises():
    exercises = []
    for doc in db.exercises.find():
        exercise = document_to_model(doc, Exercise)
        exercises.append(exercise.dict())
    return exercises


@app.post("/exercises")
def create_exercise(exercise: Exercise):
    doc = exercise.dict()
    result = db.exercises.insert_one(doc)
    if result.acknowledged:
        return {"message": "Exercise created", "id": str(result.inserted_id)}
    else:
        raise HTTPException(
            status_code=500, detail="Failed to create exercise")


@app.get("/workouts")
def get_workouts():
    workouts = []
    for doc in db.workouts.find():
        workout = document_to_model(doc, Workout)
        workouts.append(workout.dict())
    return workouts


@app.post("/workouts")
def create_workout(workout: Workout):
    doc = workout.dict()
    result = db.workouts.insert_one(doc)
    if result.acknowledged:
        return {"message": "Workout created", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create workout")


@app.get("/programs")
def get_programs():
    programs = []
    for doc in db.programs.find():
        program = document_to_model(doc, Program)
        programs.append(program.dict())
    return programs


@app.post("/programs")
def create_program(program: Program):
    doc = program.dict()
    result = db.programs.insert_one(doc)
    if result.acknowledged:
        return {"message": "Program created", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create program")
