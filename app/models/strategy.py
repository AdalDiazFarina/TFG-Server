from app_context import db

class Strategy(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  description = db.Column(db.String(255))
  Total_profitability = db.Column(db.Numeric)
  Volatility = db.Column(db.Numeric)
  Maximum_loss = db.Column(db.Numeric)
  Sharpe = db.Column(db.Numeric)
  Sortino = db.Column(db.Numeric)
  Alpha = db.Column(db.Numeric)
  Beta = db.Column(db.Numeric)
  Information_ratio = db.Column(db.Numeric)
  Success_rate = db.Column(db.Numeric)
  Portfolio_concentration_ratio = db.Column(db.Numeric)

  operations = db.relationship('Operation', lazy=True, cascade='all, delete-orphan')
