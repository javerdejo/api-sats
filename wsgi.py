"""Point of entry for gunicorn server."""
from api import app as application

if __name__ == "__main__":
    application.run()
