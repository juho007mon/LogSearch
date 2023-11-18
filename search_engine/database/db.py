

from flask_sqlalchemy import SQLAlchemy

# TODO: check with meta_db_cntlr.py
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


from database.db import db, init_db
from database.models import JiraIssue
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
init_db(app)

def update_database():
    # Logic to update database
    # For example, to add a new issue:
    new_issue = JiraIssue(jira_id='JIRA1234', status='Open')
    db.session.add(new_issue)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        update_database()