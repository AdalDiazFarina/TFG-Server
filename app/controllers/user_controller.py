from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.views.user_view_model import UserUpdateViewModel
from app.models.user import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/user', methods=['GET'])
@jwt_required()
def get():
    try:
        userid = get_jwt_identity()
        user = UserService.get_by_id(userid)
        if user['code'] == 1:
            return jsonify(code=1, message='OK', data=user['data'].to_dict()), 200
        else:
            return jsonify(code=-1, message='The user not exists'), 401
    except Exception as e:
        return jsonify(code=-2, message=f'Internal server error {e}'), 500

@user_controller.route('/user', methods=['PUT'])
@jwt_required()
def update():
    try:
        userUpdateViewModel = UserUpdateViewModel(request.get_json())
        resp = UserService.updateUser(userUpdateViewModel)
        if resp['code'] == 1:
            return jsonify(code=1, message='OK', data=resp['data'].to_dict()), 200
        else:
            return jsonify(code=-1, message='The user could not be updated'), 401 
    except Exception as e:
        return jsonify(code=-2, message=f'Internal server error {e}'), 500
  