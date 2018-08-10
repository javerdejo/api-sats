"""Simple controller."""
from flask import send_file, make_response, render_template
from flask_restful import Resource
from tokens.tokentools import verify_token


class ControllerSats(Resource):
    """Add controler for sats requests."""

    def __init__(self, **kwargs):
        """Define constructor."""
        self.model = kwargs['model']
        self.publicKey = kwargs['publicKey']

    def download(self, filename, token):
        """Download h5 file."""
        code = verify_token(token, self.model, self.publicKey)
        if code is not True:
            return code

        filename = 'files/nflh.h5'
        return make_response(send_file(filename, as_attachment=True))

    def get(self):
        """Metodo get."""
        return make_response(render_template('sats.html'))
