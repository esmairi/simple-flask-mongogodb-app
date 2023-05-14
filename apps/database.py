from pymongo import mongo_client, ASCENDING
from pymongo.database import Database

from config import settings


def get_mongo_client() -> mongo_client.MongoClient:
    client = mongo_client.MongoClient(settings.DATABASE_URL)
    print('🚀 Connected to MongoDB...')
    return client


def get_mongo_db() -> Database:
    client = get_mongo_client()
    return client[settings.MONGO_INITDB_DATABASE]
    # Note = db.notes
    # Note.create_index([("title", ASCENDING)], unique=True)

