"""Simple controller."""
from flask_restful import Resource
from tokens.tokentools import verify_token


class ControllerSats(Resource):
    """Add controler for sats requests."""

    def __init__(self, **kwargs):
        """Define constructor."""
        self.model = kwargs['model']
        self.secret = kwargs['secret']

    def get(self, token):
        """Metodo get."""
        code = verify_token(token, self.model, self.secret)
        if code is not True:
            return code

        return {'message': 'granted'}, 200
