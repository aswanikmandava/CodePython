from flask import Blueprint

main_bp = Blueprint('default', __name__)

from . import views