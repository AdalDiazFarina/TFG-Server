from database import db
from app.models.operation import Operation

class Strategy(db.Model):
  __tablename__ = 'strategy'
  
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


  def to_dict(self):
    return {
      'name': self.name,
      'description': self.description,
      'Total_profitability': float(self.Total_profitability) if self.Total_profitability is not None else None, 
      'Volatility': float(self.Volatility) if self.Volatility is not None else None,
      'Maximum_loss': float(self.Maximum_loss) if self.Maximum_loss is not None else None,
      'Sharpe': float(self.Sharpe) if self.Sharpe is not None else None,
      'Sortino': float(self.Sortino) if self.Sortino is not None else None,
      'Alpha': float(self.Alpha) if self.Alpha is not None else None,
      'Beta': float(self.Beta) if self.Beta is not None else None,
      'Information_ratio': float(self.Information_ratio) if self.Information_ratio is not None else None,
      'Success_rate': float(self.Success_rate) if self.Success_rate is not None else None,
      'Portfolio_concentration_ratio': float(self.Portfolio_concentration_ratio) if self.Portfolio_concentration_ratio is not None else None,
    }

