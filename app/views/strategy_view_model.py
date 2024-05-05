from app.models.strategy import Strategy
from app_context import api
from flask_restx import fields

strategyModelDoc = api.model('Strategy', {
    'name': fields.String(required=False, description='The name of the strategy'),
    'description': fields.String(required=False, description='Description of the strategy'),
})

class StrategyViewModel:

  def __init__(self, data):
    self.strategy = Strategy()
    self.profile_id = data['profile_id'] if data['profile_id'] is not None else -1
    self.strategy.name = data['name']
    self.strategy.description = data['description']
  
  def to_dict(self):
    return {
      'profile_id': self.profile_id,         
      'name': self.strategy.name,
      'description': self.strategy.description
    }
