from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
db = SQLAlchemy()


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  return app