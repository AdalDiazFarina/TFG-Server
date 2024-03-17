import bcrypt
from database import db
from app.models.investment_profile import InvestmentProfile

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  nickname = db.Column(db.String(255))
  email = db.Column(db.String(255))
  password_hash = db.Column(db.String(128), nullable=False)

  def set_password(self, password):
    try:
      salt = bcrypt.gensalt()
      hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
      self.password_hash = hashed_password.decode('utf-8')  # Guarda el hash como una cadena
      return {'code': 1, 'message': 'Password encrypted successfully'}
    except Exception as e:
      return {'code': -1, 'message': f'The password cannot be encrypted. {e}'}

  def check_password(self, password):
    try:
      hashed_password_bytes = self.password_hash.encode('utf-8')
      if bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes):
        return {'code': 1, 'message': 'OK'}
      else:
        return {'code': -1, 'message': 'The password is wrong'}
    except Exception as e:
      return {'code': -2, 'message': f'Something went wrong when checking the password. {e}'}

  def to_dict(self):
    return {'id': self.id, 'name': self.name, 'nickname': self.nickname, 'email': self.email}

  investment_profiles = db.relationship('InvestmentProfile', lazy=True, back_populates='user')
