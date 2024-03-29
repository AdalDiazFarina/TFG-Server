from flask import request, jsonify
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.views.user_view_model import UserUpdateViewModel, userDoc
from app.models.user import User
from app_context import api

user_ns = api.namespace('User', path='/api', description='User operations')

@user_ns.route('/user', endpoint='UserController')
class UserController(Resource):
    @user_ns.doc(description='Get a new user')
    @user_ns.doc(security='Bearer')
    @user_ns.response(200, 'Success')
    @user_ns.response(400, 'Bad Request')
    @user_ns.response(500, 'Internal Server Error')
    @jwt_required()
    def get(self):
        try:
            userid = get_jwt_identity()
            user = UserService.get_by_id(userid)
            if user['code'] == 1:
                return {'code': 1, 'message': 'OK', 'data': user['data'].to_dict()}, 200
            else:
                return {'code': -1, 'message': 'The user not exists'}, 400
        except Exception as e:
            return {'code': -2, 'message': f'Internal server error {e}'}, 500

    @user_ns.doc(description='Update a user')
    @user_ns.doc(security='Bearer')
    @user_ns.expect(userDoc)
    @user_ns.response(200, 'Success')
    @user_ns.response(400, 'Bad Request')
    @user_ns.response(500, 'Internal Server Error')
    @jwt_required()
    def put(self):
        try:
            userUpdateViewModel = UserUpdateViewModel(request.get_json())
            resp = UserService.updateUser(userUpdateViewModel)
            if resp['code'] == 1:
                user = resp['data']
                return {'code': 1, 'message': 'OK', 'data': f'{user}'}, 200
            else:
                return {'code': -1, 'message': 'The user could not be updated'}, 400
        except Exception as e:
            db.session.rollback()
            return {'code': -2, 'message': f'Internal server error {e}'}, 500