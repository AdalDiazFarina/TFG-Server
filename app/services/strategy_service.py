from database import db
from app.models.strategy import Strategy
from app_context import create_app
from flask_restx import Resource
from sqlalchemy.orm.session import Session

class StrategyService:
  app = create_app()

  @classmethod
  def get_by_id(cls, id):
    try:
      with cls.app.app_context():
        strategy = Strategy.query.get(id)
        if strategy:
          return {'code': 1, 'message': 'OK', 'data': strategy}
        else:
          return {'code': -1, 'message': 'User not found'}
    except Exception as e:
      return {'code': -1, 'message': str(e)}

  @classmethod
  def get_by_filter(cls, filters):
    try:
      with cls.app.app_context():
        query = db.session.query(Strategy)
        conditions = [getattr(Strategy, key) == value for key, value in filters.items() if hasattr(Strategy, key) and value is not None]
        filtered_query = query.filter(*conditions)
        filtered_profiles = filtered_query.all()
        if filtered_strategy:
          return {'code': 1, 'message': 'OK', 'data': filtered_strategy}
        else:
          return {'code': -1, 'message': 'No strategies found'}
    except Exception as e:
      return {'code': -2, 'message': f'Error: {e}'}


  @classmethod
  def createStrategy(cls, strategy):
    try:
      with cls.app.app_context():
          db.session.add(strategy)
          db.session.commit()
          return {'code': 1, 'message': 'OK'}
    except Exception as e:
      db.session.rollback()
      return {'code': -1, 'message': 'Error creating the strategy'}

  # @classmethod
  # def updateProfile(cls, newProfile):
  #   try:
  #     with cls.app.app_context():
  #       profile = None
  #       if newProfile.name is not None:
  #         profile = cls.get_by_filter({'name': newProfile.name})['data'][0]
          
  #       if profile and newProfile:
  #         for key, value in newProfile.to_dict().items():
  #           if hasattr(profile, key):
  #             setattr(profile, key, value)
        
  #       db.session.add(profile)
  #       db.session.commit()
  #       return {'code': 1, 'message': 'OK', 'data': profile.to_dict()}
  #   except Exception as e:
  #     db.session.rollback()
  #     return {'code': -1, 'message': f'Error updating the investment profile {e}'}

  # @classmethod
  # def deleteProfile(cls, id):
  #   try:
  #     with cls.app.app_context():
  #         profile = cls.get_by_id(id)
  #         if profile['code'] == 1:
  #           db.session.delete(profile['data'])
  #           db.session.commit()
  #           return {'code': 1, 'message': 'OK'}
  #         else:
  #           return {'code': -1, 'message': 'Profile not found'}
  #   except Exception as e:
  #     db.session.rollback()
  #     return {'code': -1, 'message': 'Error creating the investment profile'}