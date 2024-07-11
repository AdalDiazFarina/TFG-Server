from database import db
from app.models.strategy import Strategy
from app.models.investment_profile import InvestmentProfileStrategy
from app_context import create_app
from decimal import Decimal
from sqlalchemy import func
from flask_restx import Resource
from sqlalchemy.orm.session import Session

class StrategyService:
  app, socketio = create_app()

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
      with db.session() as session:
        query = session.query(Strategy, InvestmentProfileStrategy)
        if 'profile_id' in filters and filters['profile_id'] != -1:
            query = query.join(InvestmentProfileStrategy, Strategy.id == InvestmentProfileStrategy.strategy_id)
            query = query.filter(InvestmentProfileStrategy.investment_profile_id == filters['profile_id'])
        conditions = []
        for key, value in filters.items():
          if hasattr(Strategy, key):
            attribute = getattr(Strategy, key)
            if isinstance(value, int) and value != -1:
              conditions.append(attribute == value)
            elif isinstance(value, str) and value != '':
              print(f'{attribute} ilike {value.lower()}')
              conditions.append(func.lower(attribute).ilike('%' + value.lower() + '%'))
            
        if conditions:
          query = query.filter(*conditions)
        
        results = query.all()
        
        if results:
          data = []
          for strategy, profile_strategy in results:
            strategy_data = strategy.to_dict()  
            profile_strategy_data = profile_strategy.to_dict()  
            data.append({
              'strategy': strategy_data,
              'profile_strategy': profile_strategy_data
            })
            
          return {'code': 1, 'message': 'OK', 'data': data}
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

  @classmethod
  def updateStrategy(cls, newStrategy):
    try:
      with cls.app.app_context():
        strategy = None
        if newStrategy.name is not None:
          strategy = cls.get_by_filter({'name': newStrategy.strategy.name})['data'][0]
          
        if strategy and newStrategy:
          for key, value in newStrategy.strategy.to_dict().items():
            if hasattr(strategy, key):
              setattr(strategy, key, value)
        
        db.session.add(strategy)
        db.session.commit()
        return {'code': 1, 'message': 'OK', 'data': strategy.to_dict()}
    except Exception as e:
      db.session.rollback()
      return {'code': -1, 'message': f'Error updating the investment profile {e}'}

  @classmethod
  def deleteStrategy(cls, id):
    try:
      with cls.app.app_context():
          strategy = cls.get_by_id(id)
          if strategy['code'] == 1:
            db.session.delete(strategy['data'])
            db.session.commit()
            return {'code': 1, 'message': 'OK'}
          else:
            return {'code': -1, 'message': 'Strategy not found'}
    except Exception as e:
      db.session.rollback()
      return {'code': -1, 'message': 'Error deleting the strategy'}