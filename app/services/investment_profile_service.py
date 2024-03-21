from database import db
from app.models.investment_profile import InvestmentProfile
from app_context import create_app
from flask_restx import Resource

class InvestmentProfileService:
  app = create_app()

  @classmethod
  def get_by_id(cls, id):
    try:
      with cls.app.app_context():
        profile = InvestmentProfile.query.get(id)
        if profile:
          return {'code': 1, 'message': 'OK', 'data': profile}
        else:
          return {'code': -1, 'message': 'User not found'}
    except Exception as e:
      return {'code': -1, 'message': str(e)}
