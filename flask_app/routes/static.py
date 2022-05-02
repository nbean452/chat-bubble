from flask import Blueprint, redirect, render_template, url_for, send_file
from werkzeug.exceptions import HTTPException

static = Blueprint('static', __name__, url_prefix='/static')

@static.route('/<path:file>')
def profile(file):
    return send_file("/flask_app/" + file)