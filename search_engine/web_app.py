from flask import Flask
from controllers.issue_tracker_controller import IssueTrackerController

app = Flask(__name__)
issue_tracker_controller = IssueTrackerController()

@app.route('/search', methods=['GET'])
def search_issues():
    return issue_tracker_controller.search()

if __name__ == '__main__':
    app.run(debug=True)