"""Simple controller."""
from flask import render_template, make_response
from flask_restful import Resource


class ControllerHome(Resource):
    """Add controller for home requets."""

    def __init__(self, **kwargs):
        """Define constructor."""
        self.model = kwargs['model']

    def get(self):
        """Get method response."""
        self.model.insert_request(1)
        return make_response(render_template('index.html'))
