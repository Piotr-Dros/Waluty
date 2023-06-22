from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# For testing blueprint
from app.main import bp as main_bp
app.register_blueprint(main_bp)

# Blueprint here
from app.api.graphs import bp as graph_bp
app.register_blueprint(graph_bp, url_prefix='/api/graphs')

