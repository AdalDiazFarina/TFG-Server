from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
import secrets
import os
from dotenv import load_dotenv
from database import db

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)
  jwt = JWTManager(app)
  db.init_app(app)

  return app