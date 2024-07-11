from database import db
from app.models.investment_profile import InvestmentProfile, InvestmentProfileStrategy
from app.models.strategy import Strategy
from app.models.operation import Operation
from app_context import create_app, engine
from flask_restx import Resource
from sqlalchemy.orm.session import Session
from datetime import datetime, date
from sqlalchemy import func, delete
from sqlalchemy.orm import sessionmaker

class InvestmentProfileService:
  app, socketio = create_app()

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
        conditions = []
        for key, value in filters.items():
          if hasattr(InvestmentProfile, key):
            if isinstance(value, int) and value != -1:
              conditions.append(getattr(InvestmentProfile, key) == value)
            if isinstance(value, str) and value != '':
              conditions.append(func.lower(getattr(InvestmentProfile, key)).ilike('%' + value.lower() + '%'))
        filtered_query = query.filter(*conditions)
        print(*conditions)
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
        cls.associateStrategiesWithTheProfile(profile)
        return {'code': 1, 'message': 'OK'}
    except Exception as e:
      print('Error creating the investment profile')
      return {'code': -1, 'message': 'Error creating the investment profile'}

  @classmethod
  def associateStrategiesWithTheProfile(cls, profile):
    try:
      with cls.app.app_context():
        strategies = db.session.query(Strategy).all()
        print("Strategies: ", strategies)
        for strategy in strategies:
          existing_association = db.session.query(InvestmentProfileStrategy).filter_by(
            investment_profile_id=profile.id,
            strategy_id=strategy.id
          ).first()
          if existing_association:
            print("- Association between Strategy '{}' and Profile '{}' already exists.".format(strategy.name, profile.name))
          else:
            new_entry = InvestmentProfileStrategy(
              investment_profile_id=profile.id,
              strategy_id=strategy.id,
              validated=False,
              total_profitability=0.0,
              volatility=0.0,
              maximum_loss=0.0,
              sharpe=0.0,
              sortino=0.0,
              alpha=0.0,
              beta=0.0,
              information_ratio=0.0,
              success_rate=0.0,
              portfolio_concentration_ratio=0.0,
            )
            db.session.add(new_entry)
            db.session.commit()
        return {'code': 1, 'message': 'OK'}
    except Exception as e:
      print(f"Error associating profiles with strategies: {e}")
      return {'code': -1, 'message': 'Error associating profiles with strategies'}

  @classmethod
  def updateProfile(cls, newProfile):
    try:
      with cls.app.app_context():
        profile = None
        if newProfile.id is not None:
          profile = cls.get_by_filter({'id': newProfile.id})['data'][0]
        
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
          print(f'profile: ', profile)
          if profile['code'] == 1:
            investment_profile = profile['data']    
            investment_profile_id = investment_profile.id
            strategies_to_delete = db.session.query(InvestmentProfileStrategy).filter_by(investment_profile_id=investment_profile_id).all()
            operation_to_delete = db.session.query(Operation).filter_by(investment_profile_id=investment_profile_id).all()
            for operation in operation_to_delete:
              db.session.delete(operation)

            for strategy in strategies_to_delete:
              db.session.delete(strategy)

            profile_instance = profile['data']
            print(f'Deleting profile instance: {profile_instance}')
            db.session.delete(profile['data'])
            db.session.commit()
            return {'code': 1, 'message': 'OK'}
          else:
            return {'code': -1, 'message': 'Profile not found'}
    except Exception as e:
      db.session.rollback()
      print(f'Exception occurred: {str(e)}')
      return {'code': -1, 'message': 'Error deleting the investment profile'}

  @classmethod
  def deleteMultipleProfile(cls, ids):
    try:
      Session = sessionmaker(bind=engine)
      session = Session()
      session.execute(delete(InvestmentProfile).where(InvestmentProfile.id.in_(ids)))
      session.commit()
      session.close()
      return {'code': 1, 'message': 'OK'}
    except Exception as e:
      return {'code': -1, 'message': f'Error deleting investment profiles: {e}'}