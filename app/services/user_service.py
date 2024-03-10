from database import db
from app.models.user import User
from app_context import create_app

class UserService:
  app = create_app()

  @classmethod
  def get(cls, id):
    try: 
      with cls.app.app_context():
        return {'code': 1, 'message': 'OK', 'data': User.query.get(id)}
    except Exception as e:
      return {'code': -1, 'message': 'The user could not be obtained'}

  @classmethod
  def get(cls, user):
    try: 
      with cls.app.app_context():
        query = db.session.query(User)
        for key, value in user.to_dict():
          query = query.filter(getattr(User, key) == value)
        
        filtered_users = query.all()
        return {'code': 1, 'message': 'OK', 'data': filtered_users}
    except Exception as e:
      return {'code': -1, 'message': 'The user could not be obtained'}


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
        if newUser.id is not None:
          user = User.query.get(newUser.id)

        if user and newUser:
          for key, value in newUser.to_dict():
            if hasattr(user, key) and key != 'id':
              setattr(user, key, value)
        
          db.session.commit()
      
        return {'code': 1, 'message': 'OK', 'data': user}
    except Exception as e:
      return {'code': -1, 'message': 'Error updating the user'}