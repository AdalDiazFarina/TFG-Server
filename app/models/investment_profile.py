from database import db
from app.models.strategy import Strategy
from sqlalchemy import ForeignKeyConstraint

investment_profile_strategy = db.Table(
    'investment_profile_strategy',
    db.Column('investment_profile_id', db.Integer, db.ForeignKey('investment_profile.id', ondelete='CASCADE'), primary_key=True),
    db.Column('strategy_id', db.Integer, db.ForeignKey('strategy.id', ondelete='CASCADE'), primary_key=True)
)

class InvestmentProfile(db.Model):
  __tablename__ = 'investment_profile'
  
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  user = db.relationship('User', back_populates='investment_profiles')
  name = db.Column(db.String(255))
  description = db.Column(db.String(255))
  initial_capital = db.Column(db.Numeric)
  duration = db.Column(db.Date)
  monthly_contribution = db.Column(db.Numeric)

  strategies = db.relationship('Strategy', secondary=investment_profile_strategy, lazy='subquery', passive_deletes=True)

  def to_dict(self):
    return { 
      'id': self.id,
      'user_id': self.user_id,
      'name': self.name,
      'description': self.description,
      'initial_capital': float(self.initial_capital), 
      'duration': f'{self.duration}',
      'monthly_contribution': float(self.monthly_contribution)
    }

  __table_args__ = (
    ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_investment_profile_user_id'),
  )