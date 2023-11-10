from flask import Blueprint

s_bp = Blueprint('status', __name__)

from . import views

