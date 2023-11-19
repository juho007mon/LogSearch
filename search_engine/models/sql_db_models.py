
from typing import Dict
from web_app import app, db

class JiraIssue(db.Model):
    jira_id = db.Column(db.String(120), primary_key=True)

    status = db.Column(db.JSON)    # {type:bool}
    log_files = db.Column(db.JSON) # {type:path}

    def __repr__(self):
        return f'<JiraIssue {self.jira_id}>'
    
    def __init__(self, jira_id:str, status:Dict[str,str], log_files:Dict[str:str]):
        self.jira_id = jira_id
        self.status = status
        self.log_files = log_files