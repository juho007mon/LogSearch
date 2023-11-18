from flask import Blueprint

search_bp = Blueprint('issue_tracker', __name__, template_folder='templates')

from . import routes