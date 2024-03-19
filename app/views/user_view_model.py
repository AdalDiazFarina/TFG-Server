from app.models.user import User
class UserViewModel:
  user = User()

  def __init__(self, data):
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
