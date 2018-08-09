"""APIRest Full."""
from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

# loads the configuration values for the api
import config as cfg

# loads model-view-controller elements
from tokens.tokentools import load_secret_key
from models.Model import Model
from controllers.ControllerHome import ControllerHome
from controllers.ControllerSats import ControllerSats

# loads the public encryption key
secret = load_secret_key(cfg.key)

# creates flask apirest full
app = Flask(__name__)
api = Api(app)

# configures mongodb connectrion string
app.config["MONGO_URI"] = "mongodb://{}:{}@{}:{}/{}".format(cfg.username,
                                                            cfg.password,
                                                            cfg.host,
                                                            cfg.port,
                                                            cfg.dbname)
# creates the model
model = Model(PyMongo(app))

# register the api routes and controllers
api.add_resource(ControllerHome, '/',
                 resource_class_kwargs={'model': model})

api.add_resource(ControllerSats, '/sats/<token>',
                 resource_class_kwargs={'model': model, 'secret': secret})

# runs de app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
