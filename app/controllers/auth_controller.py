from flask import request
from database import db
from flask_restx import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.views.user_view_model import UserViewModel, userDoc, userDocLogin
from app.models.user import User
from app_context import api

auth_ns = api.namespace('Auth', path='/api', description='Authentication end points')

## Auth class. This class contain the authentification routes
@auth_ns.route('/register')
class RegisterController(Resource):
    @auth_ns.doc(description='Register a new user')
    @auth_ns.expect(userDoc)
    @auth_ns.response(201, 'Created')
    @auth_ns.response(400, 'Bad Request')
    @auth_ns.response(500, 'Internal Server Error')
    def post(self):
        try: 
            userViewModel = UserViewModel(request.get_json())
            filters = {'email': userViewModel.user.email, 'nickname': userViewModel.user.nickname}
            resp = UserService.get_by_filter(filters)
            if resp['code'] == 1: 
                return {'code': -1, 'message': 'The user already exists'}, 400
            UserService.createUser(userViewModel.user)
            return {'code': 1, 'message': 'User registered successfully'}, 201
        except Exception as e:
            print(f'error: {e}')
            db.session.rollback()
            return {'code': -2, 'message': 'Internal Server Error: {e}'}, 500

@auth_ns.route('/login')
class LoginController(Resource):
    @auth_ns.doc(description='Login to the application')
    @auth_ns.expect(userDocLogin)
    @auth_ns.response(200, 'Success')
    @auth_ns.response(400, 'Bad Request')
    @auth_ns.response(404, 'Unauthorized')
    @auth_ns.response(500, 'Internal Server Error')
    def post(self):
        try:
            print(f'params: {request.get_json()}')
            user_data = request.get_json()
            filters = {'nickname': user_data['nickname']}
            resp = UserService.get_by_filter(filters)
            if resp['code'] == 1:
                user = resp['data'][0]
            else:
                return {'code': -1, 'message': 'Invalid username or password'}, 400
            resp = user.check_password(user_data['password'])
            if user and resp['code'] == 1:
                print('user returned')
                access_token = create_access_token(identity=user.id)
                refresh_token = create_refresh_token(identity=user.id)
                return {'code': 1, 'messaje': 'OK', 'access_token': access_token, 'refresh_token': refresh_token}, 200
            else:
                message = resp['message']
                return {'code': -1, 'message': f'{message}'}, 404
        except Exception as e:
            return {'code': -2, 'message': f'Internal Server Error {e}'}, 500

@auth_ns.route('/refresh')
class RefreshController(Resource):
    @auth_ns.doc(description='Refresh the access token')
    @auth_ns.doc(security='Bearer')
    @auth_ns.response(404, 'Unauthorized')
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        new_refresh_token = create_refresh_token(identity=current_user)
        return {'code': 1, 'message': 'OK', 'access_token': new_access_token, 'refresh_token': new_refresh_token}, 200   