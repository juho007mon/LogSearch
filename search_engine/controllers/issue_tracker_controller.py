
from services.search_service import SearchService

class IssueTrackerController:
    def __init__(self):
        self.search_service = SearchService()

    def search(self):
        # extract query from request args
        query = 'query_placeholder'
        results = self.search_service.execute_search(query)
        return results