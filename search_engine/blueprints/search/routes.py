

from flask import render_template, request
from . import search_bp
from services.search_service import SearchService

search_service = SearchService()

@search_bp.route('/')
def index():
    return render_template('search.html')

@search_bp.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_service.search(query)
    # You might need to jsonify the results or return a render_template call
    return render_template('results.html', results=results)