from app.models.strategy import Strategy
from app_context import api
from flask_restx import fields

strategyModelDoc = api.model('Strategy', {
    'name': fields.String(required=False, description='The name of the strategy'),
    'description': fields.String(required=False, description='Description of the strategy'),
    'Total_profitability': fields.Float(required=False, description='Total profitability of the strategy'),
    'Volatility': fields.Float(required=False, description='Volatility of the strategy'),
    'Maximum_loss': fields.Float(required=False, description='Maximum loss of the strategy'),
    'Sharpe': fields.Float(required=False, description='Sharpe ratio of the strategy'),
    'Sortino': fields.Float(required=False, description='Sortino ratio of the strategy'),
    'Alpha': fields.Float(required=False, description='Alpha value of the strategy'),
    'Beta': fields.Float(required=False, description='Beta value of the strategy'),
    'Information_ratio': fields.Float(required=False, description='Information ratio of the strategy'),
    'Success_rate': fields.Float(required=False, description='Success rate of the strategy'),
    'Portfolio_concentration_ratio': fields.Float(required=False, description='Portfolio concentration ratio of the strategy')
})

class StrategyViewModel:

  def __init__(self, data):
    self.strategy = Strategy()
    self.profile_id = data['profile_id'] if data['profile_id'] is not None else -1
    self.strategy.name = data['name']
    self.strategy.description = data['description']
    self.strategy.Total_profitability = data['Total_profitability'] if data['Total_profitability'] is not None else -1
    self.strategy.Volatility = data['Volatility'] if data['Volatility'] is not None else -1
    self.strategy.Maximum_loss = data['Maximum_loss'] if data['Maximum_loss'] is not None else -1
    self.strategy.Sharpe = data['Sharpe'] if data['Sharpe'] is not None else -1
    self.strategy.Sortino = data['Sortino'] if data['Sortino'] is not None else -1
    self.strategy.Alpha = data['Alpha'] if data['Alpha'] is not None else -1
    self.strategy.Beta = data['Beta'] if data['Beta'] is not None else -1
    self.strategy.Information_ratio = data['Information_ratio'] if data['Information_ratio'] is not None else -1
    self.strategy.Success_rate = data['Success_rate'] if data['Success_rate'] is not None else -1
    self.strategy.Portfolio_concentration_ratio = data['Portfolio_concentration_ratio'] if data['Portfolio_concentration_ratio'] is not None else -1
  
  def to_dict(self):
    return {
      'profile_id': self.profile_id,         
      'name': self.strategy.name,
      'description': self.strategy.description,
      'Total_profitability': float(self.strategy.Total_profitability), 
      'Volatility': float(self.strategy.Volatility),
      'Maximum_loss': float(self.strategy.Maximum_loss),
      'Sharpe': float(self.strategy.Sharpe),
      'Sortino': float(self.strategy.Sortino),
      'Alpha': float(self.strategy.Alpha),
      'Beta': float(self.strategy.Beta),
      'Information_ratio': float(self.strategy.Information_ratio),
      'Success_rate': float(self.strategy.Success_rate),
      'Portfolio_concentration_ratio': float(self.strategy.Portfolio_concentration_ratio),
    }
