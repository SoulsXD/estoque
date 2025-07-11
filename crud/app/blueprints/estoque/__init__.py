from flask import Blueprint

bp = Blueprint('estoque', __name__, template_folder='templates')

from app.blueprints.estoque import routes