from database import db
from app.models.strategy import Strategy
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint

class InvestmentProfileStrategy(db.Model):
    __tablename__ = 'investment_profile_strategy'
    investment_profile_id = db.Column(db.Integer, db.ForeignKey('investment_profile.id'), primary_key=True)
    strategy_id = db.Column(db.Integer, db.ForeignKey('strategy.id'), primary_key=True)
    validated = db.Column(db.Boolean, nullable=False, default=False)
    total_profitability = db.Column(db.Numeric)
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
    profile = db.relationship('InvestmentProfile', backref='strategy_links')
    strategy = db.relationship('Strategy', backref='profile_links')

class InvestmentProfile(db.Model):
    __tablename__ = 'investment_profile'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    initial_capital = db.Column(db.Numeric)
    duration = db.Column(db.Date)
    monthly_contribution = db.Column(db.Numeric)

    # Relación con User
    user = db.relationship('User', back_populates='investment_profiles')

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