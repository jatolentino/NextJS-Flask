from flask import Flask
from flask_cors import CORS
#from flask_restful import Api
import multiprocessing

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    CORS(app, origins="*", supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
    #api = Api(app)
    
    # Importing the routes on function defintion to avoid circular import errors
    from .routes.main import main_bp
    from .routes.dynamo import dynamo_bp
    from .routes.cancel import cancel_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(dynamo_bp)
    app.register_blueprint(cancel_bp)

    # Setting the cancel process flag default state as False
    app.config['cancelProcess'] = multiprocessing.Value('b', False)
    
    # Default initial JSON data
    app.config['initialData'] = {
        "indexes_solution": [],
        "first_point": [],
        "fourth_point": [],
        "second_point": [],
        "third_point": []
    }

    # Global JSON data
    app.config['thedata'] = {
        "indexes_solution": [],
        "first_point": [],
        "fourth_point": [],
        "second_point": [],
        "third_point": []
    }


    return app
