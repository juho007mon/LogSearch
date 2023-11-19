

class IssueModel:
    def __init__(self, issue_data):
        self.id = issue_data['id']
        self.summary = issue_data['fields']['summary']
        # Extract other necessary fields

class LogModel:
    def __init__(self, log_data):
        self.timestamp = log_data['timestamp']
        self.message = log_data['message']
        # Extract other necessary fields
