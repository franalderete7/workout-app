import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConfigurationError
from dotenv import load_dotenv

load_dotenv()

# Get the connection string from an environment variable
COSMOS_URL = os.environ.get("COSMOS_DB_CONNECTION")
DB_NAME = os.environ.get("DATABASE_NAME")

if not COSMOS_URL or not DB_NAME:
    raise ConfigurationError(
        "Missing connection URL or database name in environment variables")

client = AsyncIOMotorClient(COSMOS_URL)
db = client.get_database(DB_NAME)
