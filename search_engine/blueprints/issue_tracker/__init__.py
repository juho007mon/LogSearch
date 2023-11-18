from flask import Blueprint

issue_tracker_bp = Blueprint('search', __name__, template_folder='templates')

from . import routes