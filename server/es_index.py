
import os

from .cfg_es import gES

from elasticsearch import helpers
from typing import List, Dict

def job_indicing(jobs : List[JobBase]):
   
# Can be nested (but avoid nesting)
# Dictionary with string, numeric , list or another dict
def index_logs():
  for root, dirs, files in os.walk('/path/to/logs'):
    for file in files:
      with open(os.path.join(root, file), 'r') as f:
        content = f.read()
        entities = gES.extract_entities(content)
        yield {
          "_op_type": 'index',
          "_index": "logs",
          "filename": file,
          "content": content,
          "entities": entities
        }

helpers.bulk(es, index_logs())


def query():
  # Search for all documents in the "people" index
  res = es.search(index="people", body={"query": {"match_all": {}}})

  # Print the search results
  for hit in res['hits']['hits']:
      print(hit["_source"])

def tagging():
  # Define a basic mapping (like a schema for the index)
  mapping = {
      "mappings": {
          "properties": {
              "name": {"type": "text"},
              "age": {"type": "integer"},
              "created_at": {"type": "date"}
          }
      }
  }

  # Create the index with the defined mapping
  index_name = "people"
  if not es.indices.exists(index=index_name):
      es.indices.create(index=index_name, body=mapping)

  # Sample data
  doc1 = {"name": "John", "age": 30, "created_at": "2023-01-10T10:00:00"}
  doc2 = {"name": "Jane", "age": 25, "created_at": "2023-02-15T12:15:00"}

  # Index the data
  es.index(index="people", body=doc1)
  es.index(index="people", body=doc2)