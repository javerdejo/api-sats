"""Simple controller."""
from flask_restful import Resource


class ControllerHome(Resource):
    """Add controller for home requets."""

    def __init__(self, **kwargs):
        """Define constructor."""
        self.model = kwargs['model']

    def get(self):
        """Metodo get."""
        self.model.insert_request(1)
        return {'message': 'sats'}, 200
