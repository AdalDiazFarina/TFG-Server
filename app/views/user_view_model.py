from app.models.user import User
class UserViewModel:
  user = User()

  def __init__(self, data):
    self.user.name = data['name']
    self.user.nickname = data['nickname']
    self.user.email = data['email']
    if data['password'] is not None:
      self.user.set_password(data['password'])