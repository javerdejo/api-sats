"""Simple controller."""
import datetime
import time
import jwt

from flask_restful import Resource
from tokens.tokentools import verify_token


class ControllerToken(Resource):
    """Add controller for home requets."""

    def __init__(self, **kwargs):
        """Define constructor."""
        self.model = kwargs['model']
        self.publicKey = kwargs['publicKey']
        self.privateKey = kwargs['privateKey']

    def get(self, id, minutes, token):
        """Get method response."""
        code = verify_token(token, self.model, self.publicKey, store=False)

        if code is not True:
            return code

        a = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
        expires = time.mktime(a.timetuple())
        token = jwt.encode({'exp': expires, 'id': id},
                           self.privateKey, algorithm='RS256')

        return "{'token': '%s'" % format(token), 200
