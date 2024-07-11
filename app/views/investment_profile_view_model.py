from app.models.investment_profile import InvestmentProfile
from app_context import api
from flask_restx import fields
from datetime import datetime

investmentProfileDoc = api.model('InvestmentProfile', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'name': fields.String(required=True, description='Name of the investment profile'),
    'description': fields.String(required=True, description='Description of the investment profile'),
    'initial_capital': fields.Float(required=True, description='Initial capital for the investment'),
    'duration': fields.Integer(required=True, description='Duration of the investment in years'),
    'monthly_contribution': fields.Float(required=True, description='Monthly contribution amount')
})

class InvestmentProfileViewModel:
  def __init__(self, data):
    self.profile = InvestmentProfile()
    self.profile.user_id = data['user_id'] if data['user_id'] is not None else -1
    self.profile.name = data['name']
    self.profile.description = data['description'] 
    self.profile.initial_capital = data['initial_capital'] if data['initial_capital'] is not None else -1
    self.profile.duration = data['duration'] if data['duration'] is not None else -1
    self.profile.monthly_contribution = data['monthly_contribution'] if data['monthly_contribution'] is not None else -1

  def to_dict():
    return {       
      'user_id': self.profile.user_id,
      'name': self.profile.name,
      'description': self.profile.description,
      'initial_capital': float(self.profile.initial_capital), 
      'duration': float(self.profile.duration),
      'monthly_contribution': float(self.profile.monthly_contribution)
    }

class UpdateInvestmentProfileViewModel:
  id = None
  name = ''
  description = ''
  initial_capital = None
  duration = None
  monthly_contribution = None

  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.description = data['description']
    self.initial_capital = data['initial_capital']
    self.duration = data['duration']
    self.monthly_contribution = data['monthly_contribution']
  
  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description, 
      'initial_capital': float(self.initial_capital), 
      'duration': self.duration, 
      'monthly_contribution': float(self.monthly_contribution)
    }