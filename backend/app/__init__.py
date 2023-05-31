from flask import Flask
from flask_cors import CORS

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object(config_class)

    # For testing blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Blueprint here
    from app.api.graphs import bp as graph_bp
    app.register_blueprint(graph_bp, url_prefix='/api/graphs')

    return app