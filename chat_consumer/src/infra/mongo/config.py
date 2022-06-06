from pymongo import MongoClient
from dynaconf import settings


def connect():
  mongo_url = f'mongodb://{settings.DB_USER_DEV}:{settings.DB_PASS_DEV}@{settings.DB_HOST_DEV}:{settings.DB_PORT_DEV}/{settings.DB_NAME_DEV}?authSource=admin'

  print(mongo_url)

  cluster = MongoClient(mongo_url, connect=False)

  db = cluster['Messages']

  return db
