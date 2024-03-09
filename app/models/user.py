from app_context import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  nickname = db.Column(db.String(255))
  email = db.Column(db.String(255))

  investment_profiles = db.relationship('InvestmentProfile', lazy=True, cascade='all, delete-orphan')
