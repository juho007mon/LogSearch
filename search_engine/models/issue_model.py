class IssueModel:
    def __init__(self, issue_data):
        self.id = issue_data['id']
        self.summary = issue_data['fields']['summary']
        # Extract other necessary fields