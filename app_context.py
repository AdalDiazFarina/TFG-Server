from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import secrets
import os
from dotenv import load_dotenv
from database import db
from flask_restx import Api

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
api = Api(version='1.0', title='Server API', description='TFG Server Api')


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)
  app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
  jwt = JWTManager(app)
  db.init_app(app)

  return app