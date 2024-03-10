from database import db

investment_profile_strategy = db.Table(
    'investment_profile_strategy',
    db.Column('investment_profile_id', db.Integer, db.ForeignKey('investment_profile.id', ondelete='CASCADE'), primary_key=True),
    db.Column('strategy_id', db.Integer, db.ForeignKey('strategy.id', ondelete='CASCADE'), primary_key=True)
)

class InvestmentProfile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_user = db.Column(db.Integer, db.ForeignKey('user.id', back_populates='investment_profiles', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String(255))
  initial_capital = db.Column(db.Numeric)
  duracion = db.Column(db.Date)
  monthly_contribution = db.Column(db.Numeric)

  strategies = db.relationship('Strategy', secondary=investment_profile_strategy, lazy=True, cascade='all, delete-orphan')