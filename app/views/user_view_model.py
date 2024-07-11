from app.models.user import User
from app_context import api
from flask_restx import fields

userDoc = api.model('User', {
    'name': fields.String(required=True, description='User name'),
    'nickname': fields.String(required=True, description='User description'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'image': fields.String(required=True, description='User profile image')
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
    self.user.image = ''
    if data['password'] is not None:
      self.user.set_password(data['password'])


class UserUpdateViewModel:
  id = ''
  name = ''
  nickname = ''
  email = ''
  image = ''

  def __init__(self, data):
    print(data)
    self.id = data['id']
    self.name = data['name']
    self.nickname = data['nickname']
    self.email = data['email']
    self.image = data['image']
  
  def to_dict(self):
    return {'id': id, 'name': self.name, 'nickname': self.nickname, 'email': self.email, 'image': self.image}
