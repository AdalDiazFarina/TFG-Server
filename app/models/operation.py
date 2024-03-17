from database import db


class Operation(db.Model):
  __tablename__ = 'operation'
  
  id = db.Column(db.Integer, primary_key=True)
  id_strategy = db.Column(db.Integer, db.ForeignKey('strategy.id', ondelete='CASCADE'))
  profit = db.Column(db.Numeric)
  start_date = db.Column(db.Date)
  end_date = db.Column(db.Date)
