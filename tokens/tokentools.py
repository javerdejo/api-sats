"""Token tools."""
import jwt


def load_secret_keys(filename):
    """Return the private key for the tokens verification."""
    global secretKey

    try:
        with open(filename+'/id_rsa.pub', 'r') as f:
            publicKey = f.read()

        with open(filename+'/id_rsa', 'r') as f:
            privateKey = f.read()

        return {'public': publicKey, 'private': privateKey}
    except OSError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)


def verify_token(token, model, secret, store=True):
    """Check the validity of the token."""
    try:
        jwt.decode(token, secret, algorithms='RS256')

        if store is True:
            if model.token_in_database(token):
                return {'message': 'Token has been used!'}, 403

            # add token into database
            model.insert_token(token)

        return True

    except jwt.exceptions.ExpiredSignatureError:
        return {'message': 'Token has expired!'}, 403

    except jwt.exceptions.InvalidTokenError:
        return {'message': 'Token is invalid!'}, 403
