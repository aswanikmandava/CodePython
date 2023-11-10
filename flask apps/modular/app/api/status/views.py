from flask import render_template
from app.api.status import s_bp


@s_bp.route("/")
def index():
    # return render_template("200.html")
    return "Welcome to status"