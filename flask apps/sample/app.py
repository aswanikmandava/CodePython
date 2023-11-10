from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return render_template('index2.html')
    except TemplateNotFound:
        return render_template('500.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal(error):
    return render_template('500.html'), 500