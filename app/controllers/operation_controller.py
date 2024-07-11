from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app_context import api, create_app
from app.views.operation_view_model import operationModelDoc
from app.services.operation_service import OperationService

app, socketio = create_app()
operation_ns = api.namespace('Operation', path='/api', description='Operation end points')

@operation_ns.route('/operation/getList')
class OperationController(Resource):
  @operation_ns.doc(description='Get all the operations')
  @operation_ns.doc(security='Bearer')
  @operation_ns.expect(operationModelDoc)
  @operation_ns.response(200, 'Sucess')
  @operation_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def post(self):
    try:
      filters = request.get_json()
      resp = OperationService.get_by_filter(filters)
      if resp['code'] == 1:
        return {'code': 1, 'message': 'OK', 'data': resp['data']}, 200
      return {'code': 1, 'message': 'Not found operations'}, 400 
    except Exception as e:
      print(f'Internal server error {e}')
      return {'code': -2, 'message': f'Internal server error {e}'}, 500