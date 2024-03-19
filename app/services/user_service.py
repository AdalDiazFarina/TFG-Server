from database import db
from app.models.user import User
from app_context import create_app

class UserService:
  app = create_app()

  @classmethod
  def get_by_id(cls, id):
    try:
      with cls.app.app_context():
        user = User.query.get(id)
        if user:
          return {'code': 1, 'message': 'OK', 'data': user}
        else:
          return {'code': -1, 'message': 'User not found'}
    except Exception as e:
      return {'code': -1, 'message': str(e)}

  @classmethod
  def get_by_filter(cls, filters):
    try:
      with cls.app.app_context():
        query = db.session.query(User)
        conditions = [getattr(User, key) == value for key, value in filters.items() if hasattr(User, key) and value is not None]
        filtered_query = query.filter(*conditions)
        filtered_users = filtered_query.all()
        if filtered_users:
          return {'code': 1, 'message': 'OK', 'data': filtered_users}
        else:
          return {'code': -1, 'message': 'No users found'}
    except Exception as e:
      return {'code': -2, 'message': f'Error: {e}'}


  @classmethod
  def createUser(cls, user):
    try:
      with cls.app.app_context():
        db.session.add(user)
        db.session.commit()
        return {'code': 1, 'message': 'OK'}
    except Exception as e:
      return {'code': -1, 'message': 'Error creating the user'}
  
  @classmethod
  def updateUser(cls, newUser):
    try:
      with cls.app.app_context():
        user = None
        if newUser.nickname is not None:
          user = cls.get_by_filter({'nickname': newUser.nickname})['data'][0]
          
        if user and newUser:
          for key, value in newUser.to_dict().items():
            if hasattr(user, key) and key != 'id':
              setattr(user, key, value)
        
          db.session.commit()
      
        return {'code': 1, 'message': 'OK', 'data': user}
    except Exception as e:
      return {'code': -1, 'message': 'Error updating the user'}