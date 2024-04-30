from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from app.services.strategy_service import StrategyService
from app_context import api, create_app
from app.views.strategy_view_model import StrategyViewModel, strategyModelDoc
from app.services.kafka_service import KafkaService

app, socketio = create_app()
strategy_ns = api.namespace('Strategy', path='/api', description='Strategy end points')

@socketio.on('run_task')
def handle_run_task():
    kafkaService = KafkaService()
    kafkaService.send('Task', 'hola')
    message = kafka_service.receive()
    if message['code'] == 1:
      emit('taskCompleted', 'completado')

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

@strategy_ns.route('/strategy/getList')
class InvestmentProfileWithoutIdController(Resource):
  @strategy_ns.doc(description='Get all the strategies')
  @strategy_ns.doc(security='Bearer')
  @strategy_ns.expect(strategyModelDoc)
  @strategy_ns.response(200, 'Sucess')
  @strategy_ns.response(500, 'Internal Server Error')
  @jwt_required()
  def post(self):
    try:
      strategyViewModel = StrategyViewModel(request.get_json())
      resp = StrategyService.get_by_filter(strategyViewModel.to_dict())
      if resp['code'] == 1:
        result = []
        for strategy in resp['data']:
          result.append(strategy.to_dict())
        return {'code': 1, 'message': 'OK', 'data': result}, 200
      return {'code': 1, 'message': 'Not found strategies'}, 200
    except Exception as e:
      print(e)
      return {'code': -2, 'message': f'Internal server error {e}'}, 500

