from jira import JIRA

class JiraClient:
    def __init__(self, server, username, password):
        self.jira = JIRA(server, basic_auth=(username, password))

    def get_issues(self, jql, max_results):
        return self.jira.search_issues(jql_str=jql, maxResults=max_results)
