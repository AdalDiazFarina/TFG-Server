from database import db
from app.models.operation import Operation

class Strategy(db.Model):
  __tablename__ = 'strategy'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  description = db.Column(db.String(255))
  model = db.Column(db.String(255))

  operations = db.relationship('Operation', lazy=True, cascade='all, delete-orphan')


  def to_dict(self):
    return {
      'name': self.name,
      'description': self.description,
      'model': self.model
    }

