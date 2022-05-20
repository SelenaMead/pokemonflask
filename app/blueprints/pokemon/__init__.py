from flask import Blueprint

bp = Blueprint('pokemon', __name__, template_folder='pokemon', url_prefix='/')

from .import routes 