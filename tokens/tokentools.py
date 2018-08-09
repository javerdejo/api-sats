"""Token tools."""
import jwt


def load_secret_key(filename):
    """Return the private key for the tokens verification."""
    global secretKey

    try:
        with open(filename, 'r') as f:
            secretKey = f.read()

        return secretKey
    except OSError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)


def verify_token(token, model, secret):
    """Check the validity of the token."""
    try:
        jwt.decode(token, secret, algorithms='RS256')

        if model.token_in_database(token):
            return {'message': 'Token has been used!'}, 403

        # add token into database
        model.insert_token(token)
        return True

    except jwt.exceptions.ExpiredSignatureError:
        return {'message': 'Token has expired!'}, 403

    except jwt.exceptions.InvalidTokenError:
        return {'message': 'Token is invalid!'}, 403
