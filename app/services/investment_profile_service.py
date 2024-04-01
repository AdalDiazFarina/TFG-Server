from database import db
from app.models.investment_profile import InvestmentProfile
from app_context import create_app
from flask_restx import Resource
from sqlalchemy.orm.session import Session
from datetime import datetime

class InvestmentProfileService:
  app = create_app()

  @classmethod
  def get_by_id(cls, id):
    try:
      with cls.app.app_context():
        profile = InvestmentProfile.query.get(id)
        if profile:
          return {'code': 1, 'message': 'OK', 'data': profile}
        else:
          return {'code': -1, 'message': 'Profile not found'}
    except Exception as e:
      return {'code': -1, 'message': str(e)}

  @classmethod
  def get_by_filter(cls, filters):
    try:
      with cls.app.app_context():
        query = db.session.query(InvestmentProfile)
        conditions = [getattr(InvestmentProfile, key) == value for key, value in filters.items() if hasattr(InvestmentProfile, key) and value != -1 and value > datetime.now().isoformat()]
        filtered_query = query.filter(*conditions)
        filtered_profiles = filtered_query.all()
        if filtered_profiles:
          return {'code': 1, 'message': 'OK', 'data': filtered_profiles}
        else:
          return {'code': -1, 'message': 'No investment profiles found'}
    except Exception as e:
      return {'code': -2, 'message': f'Error: {e}'}


  @classmethod
  def createProfile(cls, profile):
    try:
      with cls.app.app_context():
          db.session.add(profile)
          db.session.commit()
          return {'code': 1, 'message': 'OK'}
    except Exception as e:
      db.session.rollback()
      return {'code': -1, 'message': 'Error creating the investment profile'}

  @classmethod
  def updateProfile(cls, newProfile):
    try:
      with cls.app.app_context():
        profile = None
        if newProfile.name is not None:
          profile = cls.get_by_filter({'name': newProfile.name})['data'][0]
          
        if profile and newProfile:
          for key, value in newProfile.to_dict().items():
            if hasattr(profile, key):
              setattr(profile, key, value)
        
        db.session.add(profile)
        db.session.commit()
        return {'code': 1, 'message': 'OK', 'data': profile.to_dict()}
    except Exception as e:
      db.session.rollback()
      return {'code': -1, 'message': f'Error updating the investment profile {e}'}

  @classmethod
  def deleteProfile(cls, id):
    try:
      with cls.app.app_context():
          profile = cls.get_by_id(id)
          if profile['code'] == 1:
            db.session.delete(profile['data'])
            db.session.commit()
            return {'code': 1, 'message': 'OK'}
          else:
            return {'code': -1, 'message': 'Profile not found'}
    except Exception as e:
      db.session.rollback()
      return {'code': -1, 'message': 'Error deleting the investment profile'}