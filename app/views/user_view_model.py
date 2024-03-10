class UserViewModel:
  User user

  def __init__(self, data):
    user = User(name=data['name'], nickname=data['nickname'], email=data['email'])
    user.set_password(data['password'])