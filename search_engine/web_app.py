
from flask import Flask

from ip_config import IPConfig

from controllers.issue_tracker_controller import IssueTrackerController
from blueprints.search import search_bp
from blueprints.issue_tracker import issue_tracker_bp


app = Flask(__name__)
db_path = IPConfig.SQL_DB_FILE
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

issue_tracker_controller = IssueTrackerController()

@app.route('/search', methods=['GET'])
def search_issues():
    return issue_tracker_controller.search()

if __name__ == '__main__':
    app.run(debug=True)