from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.services.strategy_service import StrategyService
from app_context import api

strategy_ns = api.namespace('Strategy', path='/api', description='Strategy operations')

@strategy_ns.route('/strategy/<int:id>')
class StrategyController(Resource):
  @strategy_ns.doc(description='Get a strategy by id')
  @strategy_ns.param('id', 'The ID of the strategy', _in='path', required=True, type='integer')
  @strategy_ns.doc(security='Bearer')
  @strategy_ns.response(200, 'Success')
  @strategy_ns.response(400, 'Bad Request')
  @strategy_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def get(self, id):
    try:
      strategy = StrategyService.get_by_id(id)
      if strategy['code'] == 1:
        return {'code': 1, 'message': 'OK', 'data': strategy['data'].to_dict()}, 200
      else:
        return {'code': -1, 'message': 'The strategy not exists'}, 400
    except Exception as e:
      return {'code': -2, 'message': f'Internal server error {e}'}, 500

  @strategy_ns.doc(description='Delete a strategy by id')
  @strategy_ns.param('id', 'The ID of the strategy', _in='path', required=True, type='integer')
  @strategy_ns.doc(security='Bearer')
  @jwt_required()
  @strategy_ns.response(200, 'Success')
  @strategy_ns.response(400, 'Bad Request')
  @strategy_ns.response(500, 'Internal Server Error')
  def delete(self, id):
    # try:
    #   resp = InvestmentProfileService.deleteProfile(id)
    #   if resp['code'] == 1:
    #     return {'code': 1, 'message': 'OK', 'data': {}}, 200
    #   else:
    #     return {'code': -1, 'message': 'The investment profile could not be deleted'}, 400
    # except Exception as e:
    return {'code': -2, 'message': f'Internal server error {e}'}, 500

@strategy_ns.route('/strategy')
class StrategyWithoutIdController(Resource):
  @strategy_ns.doc(description='Create a new strategy')
  @strategy_ns.doc(security='Bearer')
  # @strategy_ns.expect(investmentProfileDoc)
  @strategy_ns.response(201, 'Created')
  @strategy_ns.response(400, 'Bad Request')
  @strategy_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def post(self):
    # try:
    #   investmentProfileViewModel = InvestmentProfileViewModel(request.get_json())
    #   filters = {'name': investmentProfileViewModel.profile.name}
    #   resp = InvestmentProfileService.get_by_filter(filters)
    #   print(resp)
    #   if resp['code'] == 1: 
    #     return {'code': -1, 'message': 'The investment profile already exists'}, 400
    #   InvestmentProfileService.createProfile(investmentProfileViewModel.profile)
    #   return {'code': 1, 'message': 'OK'}, 201
    # except Exception as e:
    return {'code': -2, 'message': f'Internal server error {e}'}, 500
  
  @strategy_ns.doc(description='Update a strategy')
  # @strategy_ns.expect(investmentProfileDoc)
  @strategy_ns.doc(security='Bearer')
  @strategy_ns.response(200, 'Success')
  @strategy_ns.response(400, 'Bad Request')
  @strategy_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def put(self):
    # try:
    #   updateInvestmentProfileViewModel = UpdateInvestmentProfileViewModel(request.get_json())
    #   resp = InvestmentProfileService.updateProfile(updateInvestmentProfileViewModel)
    #   if resp['code'] == 1:
    #     profile = resp['data']
    #     return {'code': 1, 'message': 'OK', 'data': f'{profile}'}, 200
    #   else:
    #     return {'code': -1, 'message': 'The investment profile could not be updated. ' + resp['message']}, 400 
    # except Exception as e:
    return {'code': -2, 'message': f'Internal server error {e}'}, 500