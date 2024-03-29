from app.models.investment_profile import InvestmentProfile
from app_context import api
from flask_restx import fields

investmentProfileDoc = api.model('InvestmentProfile', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'name': fields.String(required=True, description='Name of the investment profile'),
    'initial_capital': fields.Float(required=True, description='Initial capital for the investment'),
    'duration': fields.Integer(required=True, description='Duration of the investment in months'),
    'monthly_contribution': fields.Float(required=True, description='Monthly contribution amount')
})

class InvestmentProfileViewModel:
  profile = InvestmentProfile()

  def __init__(self, data):
    self.profile.user_id = data['user_id']
    self.profile.name = data['name']
    self.profile.initial_capital = data['initial_capital']
    self.profile.duration = data['duration']
    self.profile.monthly_contribution = data['monthly_contribution']

class UpdateInvestmentProfileViewModel:
  name = ''
  initial_capital = None
  duration = None
  monthly_contribution = None

  def __init__(self, data):
    self.name = data['name']
    self.initial_capital = data['initial_capital']
    self.duration = data['duration']
    self.monthly_contribution = data['monthly_contribution']
  
  def to_dict(self):
    return {'name': self.name, 'initial_capital': self.initial_capital, 'duration': self.duration, 'monthly_contribution': self.monthly_contribution}