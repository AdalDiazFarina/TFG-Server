from app_context import api
from flask_restx import fields

operationModelDoc = api.model('Operation', {
    'strategy_id': fields.String(required=False, description='The unique identificator of a strategy'),
    'profile_id': fields.String(required=False, description='The unique identificator of a profile'),
})
