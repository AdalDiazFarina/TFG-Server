from app.models.user import User
from app_context import api
from flask_restx import fields

userDoc = api.model('User', {
    'name': fields.String(required=True, description='User name'),
    'nickname': fields.String(required=True, description='User description'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

userDocLogin = api.model('UserLogin', {
    'nickname': fields.String(required=True, description='User description'),
    'password': fields.String(required=True, description='User password')
})

class UserViewModel:
  def __init__(self, data):
    self.user = User()
    self.user.name = data['name']
    self.user.nickname = data['nickname']
    self.user.email = data['email']
    if data['password'] is not None:
      self.user.set_password(data['password'])


class UserUpdateViewModel:
  name = ''
  nickname = ''
  email = ''

  def __init__(self, data):
    self.name = data['name']
    self.nickname = data['nickname']
    self.email = data['email']
  
  def to_dict(self):
    return {'name': self.name, 'nickname': self.nickname, 'email': self.email}
