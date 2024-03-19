from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.views.user_view_model import UserViewModel, UserUpdateViewModel
from app.models.user import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/register', methods=['POST'])
def register():
    try: 
        userViewModel = UserViewModel(request.get_json())
        filters = {'email': userViewModel.user.email, 'nickname': userViewModel.user.nickname}
        resp = UserService.get_by_filter(filters)
        if resp['code'] == 1: 
            return jsonify(code=-1, message='The user already exists'), 400
        UserService.createUser(userViewModel.user)
        return jsonify(code=1, message='User registered successfully'), 201
    except Exception as e:
        return jsonify(code=-2, message=f'Internal Server Error: {e}'), 500

@user_controller.route('/login', methods=['POST'])
def login():
    try:
        user_data = request.get_json()
        filters = {'nickname': user_data['nickname']}
        resp = UserService.get_by_filter(filters)
        if resp['code'] == 1:
            user = resp['data'][0]
        else:
            return jsonify(code=-1, message='Invalid username or password'), 401
        resp = user.check_password(user_data['password'])
        if user and resp['code'] == 1:
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return jsonify(code=1, messaje='OK', access_token=access_token, refresh_token=refresh_token), 200
        else:
            message = resp['message']
            return jsonify(code=-1, message=f'{message}'), 401
    except Exception as e:
        return jsonify(code=-2, message=f'Internal Server Error {e}'), 500


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
    
@user_controller.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    new_refresh_token = create_refresh_token(identity=current_user)
    return jsonify(code=1, message='OK', access_token=new_access_token, refresh_token=new_refresh_token), 200

  