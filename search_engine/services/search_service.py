from elasticsearch import Elasticsearch

class SearchService:
    def __init__(self):
        self.client = Elasticsearch(['localhost'], port=9200)

    def search(self, query):
        response = self.client.search(
            index="your_index",  # Replace with your index name
            body={
                "query": {
                    "match": {
                        "content": query  # Assuming you're searching a field named 'content'
                    }
                }
            }
        )
        # Process the response and return a list of results
        return response['hits']['hits']
