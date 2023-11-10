
from elasticsearch import Elasticsearch

class ElasticsearchManager:
    def __init__(self, config):
        self.es = Elasticsearch([{'host': config['HOST'], 'port': config['PORT']}])

    def index_document(self, index, doc_type, document):
        response = self.es.index(index=index, doc_type=doc_type, body=document)
        return response

    def search_documents(self, index, query):
        response = self.es.search(index=index, body=query)
        return response

    def execute_search(self, query):
        response = self.search_documents("dummy",query)
        return response
    