from flask import Blueprint

bp = Blueprint('main', __name__, template_folder='main', url_prefix='/')

from .import routes 