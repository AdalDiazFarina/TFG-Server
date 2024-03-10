from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from app.services.user_service import UserService
from app.views.

@app.route('/register', methods=['POST'])
def register():
    UserViewModel(request.get_json())
    UserService.createUser(UserViewModel.user)
    return jsonify(message='User registered successfully'), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(name=data['name']).first()

    if user and bcrypt.check_password(user.password_hash, data['password']):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify(message='Invalid username or password'), 401

@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required()
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    new_refresh_token = create_refresh_token(identity=current_user)
    return jsonify(access_token=new_access_token, refresh_token=new_refresh_token), 200

  