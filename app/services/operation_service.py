from database import db
from app_context import create_app
from app.models.operation import Operation

class OperationService:
  app, socketio = create_app()
  @classmethod
  def get_by_filter(cls, filters):
    try:
      with db.session() as session:
        query = session.query(Operation)
        filtered_query = query.filter_by(**filters)
        filtered_operations = filtered_query.all()
        operations_data = []
        for operation in filtered_operations:
          operations_data.append({
            'id': operation.id,
            'asset': operation.asset,
            'operation_date': operation.operation_date.strftime('%Y-%m-%d %H:%M:%S'),
            'operation_type': operation.operation_type.value, 
            'amount': float(operation.amount),
            'unit_price': float(operation.unit_price),
            'total_return': float(operation.total_return),
            'period': operation.period.value,
            'investment_profile_id': operation.investment_profile_id,
            'strategy_id': operation.strategy_id
          })
        
        if operations_data:
          return {'code': 1, 'message': 'OK', 'data': operations_data}
        else:
          print("No operations found")
          return {'code': -1, 'message': 'No operations found'}
    except Exception as e:
      print(f'Error retrieving operations: {e}')
      return {'code': -2, 'message': f'Error: {e}'}