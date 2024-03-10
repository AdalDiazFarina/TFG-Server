import bcrypt
from database import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  nickname = db.Column(db.String(255))
  email = db.Column(db.String(255))
  password_hash = db.Column(db.String(128), nullable=False)  

  def set_password(self, password):
    try:
      self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    except Exception as e:
      print({'Error assigning password to user'})

  def check_password(self, password):
    return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

  def to_dict(self):
    return {'id': self.id, 'name': self.name, 'nickname': self.nickname, 'email': self.email}

  # investment_profiles = db.relationship('InvestmentProfile', lazy=True, cascade='all, delete-orphan', back_populates='user')
