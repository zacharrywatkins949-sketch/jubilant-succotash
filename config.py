import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG', 'false').lower() in ['true', '1', 't']
    TESTING = os.environ.get('TESTING', 'false').lower() in ['true', '1', 't']
    DATABASE_URL = os.environ.get('DATABASE_URL')
    JSON_SORT_KEYS = False
