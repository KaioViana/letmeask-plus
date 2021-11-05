from pymongo import MongoClient
from dynaconf import settings


def connect():
  cluster = MongoClient(settings.MONGO_DATABASE_URL, connect=False)
  db = cluster['Messages']

  return db
