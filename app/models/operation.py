from database import db
from sqlalchemy.types import Enum
from sqlalchemy import ForeignKeyConstraint
import enum

class PeriodEnum(enum.Enum):
    period_1 = 'Period 1'
    period_2 = 'Period 2'
    period_3 = 'Period 3'

class Operation(db.Model):
    __tablename__ = 'operation'
  
    id = db.Column(db.Integer, primary_key=True)
    asset = db.Column(db.String(100), nullable=False)
    operation_date = db.Column(db.DateTime, nullable=False)
    operation_type = db.Column(Enum('buy', 'sell', name='operation_type'), nullable=False)
    amount = db.Column(db.Numeric(15, 2), nullable=False)
    unit_price = db.Column(db.Numeric(15, 2), nullable=False)
    total_return = db.Column(db.Numeric(15, 2), nullable=False)
    period = db.Column(Enum('Period 1', 'Period 2', 'Period 3', name='period'), nullable=False)
    
    investment_profile_id = db.Column(db.Integer, nullable=False)
    strategy_id = db.Column(db.Integer, nullable=False)
    
    investment_profile_strategy = db.relationship('InvestmentProfileStrategy', backref='operations')

    __table_args__ = (
        ForeignKeyConstraint(
            ['investment_profile_id', 'strategy_id'],
            ['investment_profile_strategy.investment_profile_id', 'investment_profile_strategy.strategy_id'],
            name='fk_operation_investment_profile_strategy'
        ),
    )

