import firebase_admin
from json import dumps
from dynaconf import settings
from firebase_admin import credentials
from firebase_admin import db


def connect():
  cred = credentials.Certificate(settings.FIREBASE_CONFIG_AUTH)

  firebase_admin.initialize_app(cred, { 'databaseURL': settings.FIREBASE_DATABASE_URL })
  
  return db
