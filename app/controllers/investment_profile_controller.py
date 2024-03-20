from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from app.services.investment_profile_service import InvestmentProfileService

investment_profile_controller = Blueprint('investment_profile_controller', __name__)

@investment_profile_controller.route('/investment-profile/<int:id>', methods=['GET'])
@jwt_required()
def get(id):
  try:
    profile = InvestmentProfileService.get_by_id(id)
    if profile['code'] == 1:
      return jsonify(code=1, message='OK', data=profile['data'].to_dict()), 200
    else:
      return jsonify(code=-1, message='The profile not exists'), 401
  except Exception as e:
    return jsonify(code=-2, message=f'Internal server error {e}'), 500