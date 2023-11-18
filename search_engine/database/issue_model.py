
from .db import db

class IssueModel:
    def __init__(self, issue_data):
        self.id = issue_data['id']
        self.summary = issue_data['fields']['summary']
        # Extract other necessary fields


class JiraIssue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jira_id = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(80), nullable=False)
    # Add other metadata fields

    def __repr__(self):
        return f'<JiraIssue {self.jira_id}>'