import firebase_admin
from dynaconf import settings
from firebase_admin import credentials
from firebase_admin import db

print('imported')
def connect():
  cred = credentials.Certificate(settings.FIREBASE_CONFIG_PATH)

  firebase_admin.initialize_app(cred, { 'databaseURL': settings.FIREBASE_DATABASE_URL })

  print('dataBaseInitialized******')

  return db