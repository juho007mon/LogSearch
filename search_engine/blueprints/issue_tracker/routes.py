

from flask import render_template, request
from . import issue_tracker_bp
from controllers.issue_tracker_controller import IssueTrackerController

issue_tracker_controller = IssueTrackerController()

@issue_tracker_bp.route('/')
def index():
    return render_template('issue_tracker.html')

@issue_tracker_bp.route('/issue_tracker', methods=['GET','POST'])
def search():
    return issue_tracker_controller.search()
