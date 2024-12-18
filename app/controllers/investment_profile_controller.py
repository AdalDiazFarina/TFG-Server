from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.services.investment_profile_service import InvestmentProfileService
from app.views.investment_profile_view_model import InvestmentProfileViewModel, investmentProfileDoc, UpdateInvestmentProfileViewModel
from app_context import api

profile_ns = api.namespace('Investment profile', path='/api', description='Investment profile end points')

@profile_ns.route('/investmentprofile/<int:id>')
class InvestmentProfileController(Resource):
  @profile_ns.doc(description='Get a investment profile by id')
  @profile_ns.param('id', 'The ID of the investment profile', _in='path', required=True, type='integer')
  @profile_ns.doc(security='Bearer')
  @profile_ns.response(200, 'Success')
  @profile_ns.response(400, 'Bad Request')
  @profile_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def get(self, id):
    try:
      profile = InvestmentProfileService.get_by_id(id)
      if profile['code'] == 1:
        return {'code': 1, 'message': 'OK', 'data': profile['data'].to_dict()}, 200
      else:
        return {'code': -1, 'message': 'The profile not exists'}, 400
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500

  @profile_ns.doc(description='Delete a investment profile by id')
  @profile_ns.param('id', 'The ID of the investment profile', _in='path', required=True, type='integer')
  @profile_ns.doc(security='Bearer')
  @jwt_required()
  @profile_ns.response(200, 'Success')
  @profile_ns.response(400, 'Bad Request')
  @profile_ns.response(500, 'Internal Server Error')
  def delete(self, id):
    try:
      resp = InvestmentProfileService.deleteProfile(id)
      if resp['code'] == 1:
        return {'code': 1, 'message': 'OK', 'data': {}}, 200
      else:
        return {'code': -1, 'message': 'The investment profile could not be deleted'}, 400
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500

@profile_ns.route('/investmentprofile')
class InvestmentProfileWithoutIdController(Resource):
  @profile_ns.doc(description='Create a new investment profile')
  @profile_ns.doc(security='Bearer')
  @profile_ns.expect(investmentProfileDoc)
  @profile_ns.response(201, 'Created')
  @profile_ns.response(400, 'Bad Request')
  @profile_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def post(self):
    try:
      investmentProfileViewModel = InvestmentProfileViewModel(request.get_json())
      InvestmentProfileService.createProfile(investmentProfileViewModel.profile)
      return {'code': 1, 'message': 'OK'}, 201
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500
  
  @profile_ns.doc(description='Update a investment profile')
  @profile_ns.expect(investmentProfileDoc)
  @profile_ns.doc(security='Bearer')
  @profile_ns.response(200, 'Success')
  @profile_ns.response(400, 'Bad Request')
  @profile_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def put(self):
    try:
      updateInvestmentProfileViewModel = UpdateInvestmentProfileViewModel(request.get_json())
      resp = InvestmentProfileService.updateProfile(updateInvestmentProfileViewModel)
      if resp['code'] == 1:
        profile = resp['data']
        return {'code': 1, 'message': 'OK', 'data': f'{profile}'}, 200
      else:
        return {'code': -1, 'message': 'The investment profile could not be updated. ' + resp['message']}, 400 
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500
  
  @profile_ns.doc(description='Delete a investment profile by id')
  @profile_ns.param('id', 'The ID of the investment profile', _in='path', required=True, type='integer')
  @profile_ns.doc(security='Bearer')
  @jwt_required()
  @profile_ns.response(200, 'Success')
  @profile_ns.response(400, 'Bad Request')
  @profile_ns.response(500, 'Internal Server Error')
  def delete(self):
    try:
      ids = request.json
      resp = InvestmentProfileService.deleteMultipleProfile(ids)
      if resp['code'] == 1:
        return {'code': 1, 'message': 'OK', 'data': {}}, 200
      else:
        return {'code': -1, 'message': 'The investment profiles could not be deleted'}, 400
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500

@profile_ns.route('/investmentprofile/getList')
class InvestmentProfileWithoutIdController(Resource):
  @profile_ns.doc(description='Get all the investment profiles')
  @profile_ns.doc(security='Bearer')
  @profile_ns.expect(investmentProfileDoc)
  @profile_ns.response(200, 'Sucess')
  @profile_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def post(self):
    try:
      investmentProfileViewModel = InvestmentProfileViewModel(request.get_json())
      resp = InvestmentProfileService.get_by_filter(investmentProfileViewModel.profile.to_dict())
      if resp['code'] == 1:
        result = []
        for profile in resp['data']:
          result.append(profile.to_dict())
        return {'code': 1, 'message': 'OK', 'data': result}, 200
      return {'code': 1, 'message': 'Not found investments profiles'}, 200
    except Exception as e:
      print(e)
      return {'code': -2, 'message': f'Internal server error {e}'}, 500