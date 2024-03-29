from app.models.strategy import Strategy
from app_context import api
from flask_restx import fields

strategyModelDoc = api.model('Strategy', {
    'name': fields.String(required=True, description='The name of the strategy'),
    'description': fields.String(required=True, description='Description of the strategy'),
    'Total_profitability': fields.Float(required=True, description='Total profitability of the strategy'),
    'Volatility': fields.Float(required=True, description='Volatility of the strategy'),
    'Maximum_loss': fields.Float(required=True, description='Maximum loss of the strategy'),
    'Sharpe': fields.Float(required=True, description='Sharpe ratio of the strategy'),
    'Sortino': fields.Float(required=True, description='Sortino ratio of the strategy'),
    'Alpha': fields.Float(required=True, description='Alpha value of the strategy'),
    'Beta': fields.Float(required=True, description='Beta value of the strategy'),
    'Information_ratio': fields.Float(required=True, description='Information ratio of the strategy'),
    'Success_rate': fields.Float(required=True, description='Success rate of the strategy'),
    'Portfolio_concentration_ratio': fields.Float(required=True, description='Portfolio concentration ratio of the strategy')
})

class StrategyViewModel:
  strategy = Strategy()

  def __init__(self, data):
    self.strategy.name = data['name']
    self.strategy.description = data['description']
    self.strategy.Total_profitability = data['Total_profitability']
    self.strategy.Volatility = data['Volatility']
    self.strategy.Maximum_loss = data['Maximum_loss']
    self.strategy.Sharpe = data['Sharpe']
    self.strategy.Sortino = data['Sortino']
    self.strategy.Alpha = data['Alpha']
    self.strategy.Beta = data['Beta']
    self.strategy.Information_ratio = data['Information_ratio']
    self.strategy.Success_rate = data['Success_rate']
    self.strategy.Portfolio_concentration_ratio = data['Portfolio_concentration_ratio']
    