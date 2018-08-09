"""Generates a new token."""
import datetime
import time
import jwt


def main():
    """Generate token."""
    with open('../keys/id_rsa', 'r') as f:
        secret = f.read()

    try:
        minutes = int(raw_input("Minutes duration for token? "))
    except ValueError:
        print 'Please enter an integer'
        exit(1)

    id = '1'
    a = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    expires = time.mktime(a.timetuple())
    token = jwt.encode({'exp': expires, 'id': id}, secret, algorithm='RS256')

    print token


if __name__ == "__main__":
    main()
