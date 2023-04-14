from flask import Blueprint

blueprint = Blueprint('cookies', __name__)

from . import routes, models
