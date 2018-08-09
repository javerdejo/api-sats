"""SimpleModel class."""


class Model:
    """Class for bucket storage."""

    def __init__(self, mongo):
        """Define constructor."""
        self.mongo = mongo

    def insert_request(self, typeRequest):
        """Insert new token in the database."""
        requests = self.mongo.db.requests
        requests.insert({'request': 1, 'type': typeRequest})

    def insert_token(self, token):
        """Insert new token in the database."""
        tokens = self.mongo.db.tokens
        tokens.insert({'token': token})

    def token_in_database(self, token):
        """Find a token into databse."""
        tokens = self.mongo.db.tokens
        res = tokens.find_one({'token': token})

        if res:
            return True

        return False
