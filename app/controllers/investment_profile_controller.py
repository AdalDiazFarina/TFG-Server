from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.services.investment_profile_service import InvestmentProfileService
from app_context import api

profile_ns = api.namespace('Investment profile', path='/api', description='Investment profile operations')

@profile_ns.route('/investmentprofile/<int:id>')
class InvestmentProfileController(Resource):
  @profile_ns.doc(description='Get a investment profile by id')
  @profile_ns.doc(params={'id': 'The ID of the investment profile'})
  @jwt_required()
  def get(self, id):
    try:
      profile = InvestmentProfileService.get_by_id(id)
      if profile['code'] == 1:
        return {'code': 1, 'message': 'OK', 'data': profile['data'].to_dict()}, 200
      else:
        return {'code': -1, 'message': 'The profile not exists'}, 401
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500