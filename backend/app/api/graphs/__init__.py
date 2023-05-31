from flask import Blueprint

bp = Blueprint('graphs', __name__)

from app.api.graphs import routes