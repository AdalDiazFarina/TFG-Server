from database import db
from app.models.strategy import Strategy
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint

from database import db

class InvestmentProfile(db.Model):
    __tablename__ = 'investment_profile'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    initial_capital = db.Column(db.Numeric)
    duration = db.Column(db.Numeric)
    monthly_contribution = db.Column(db.Numeric)

    # Relación con User
    user = db.relationship('User', backref='profiles')

    def to_dict(self):
        return { 
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'initial_capital': float(self.initial_capital) if self.initial_capital is not None else None,
            'duration': float(self.duration) if self.duration is not None else None,
            'monthly_contribution': float(self.monthly_contribution) if self.monthly_contribution is not None else None
        }

    __table_args__ = (
        db.UniqueConstraint('user_id', 'name', name='unique_user_profile_name'),
    )


class InvestmentProfileStrategy(db.Model):
    __tablename__ = 'investment_profile_strategy'
    investment_profile_id = db.Column(db.Integer, db.ForeignKey('investment_profile.id'), primary_key=True)
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategy.id'), primary_key=True)
    validated = db.Column(db.Boolean, nullable=False, default=False)
    total_profitability = db.Column(db.Numeric)
    annual_return = db.Column(db.Numeric)
    volatility = db.Column(db.Numeric)
    maximum_loss = db.Column(db.Numeric)
    sharpe = db.Column(db.Numeric)
    sortino = db.Column(db.Numeric)
    alpha = db.Column(db.Numeric)
    beta = db.Column(db.Numeric)
    information_ratio = db.Column(db.Numeric)
    success_rate = db.Column(db.Numeric)
    portfolio_concentration_ratio = db.Column(db.Numeric)
    
    # Definir relaciones
    profile = db.relationship('InvestmentProfile', backref='strategies')
    strategy = db.relationship('Strategy', backref='profiles')

    def to_dict(self):
        return {
            'investment_profile_id': self.investment_profile_id,
            'strategy_id': self.strategy_id,
            'validated': self.validated,
            'total_profitability': float(self.total_profitability) if self.total_profitability is not None else None,
            'volatility': float(self.volatility) if self.volatility is not None else None,
            'maximum_loss': float(self.maximum_loss) if self.maximum_loss is not None else None,
            'sharpe': float(self.sharpe) if self.sharpe is not None else None,
            'sortino': float(self.sortino) if self.sortino is not None else None,
            'alpha': float(self.alpha) if self.alpha is not None else None,
            'beta': float(self.beta) if self.beta is not None else None,
            'information_ratio': float(self.information_ratio) if self.information_ratio is not None else None,
            'success_rate': float(self.success_rate) if self.success_rate is not None else None,
            'portfolio_concentration_ratio': float(self.portfolio_concentration_ratio) if self.portfolio_concentration_ratio is not None else None,
            'annual_return': float(self.annual_return) if self.annual_return is not None else None,
        }
