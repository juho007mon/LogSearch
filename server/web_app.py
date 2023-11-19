

from flask import Flask, request, jsonify


@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword missing"}), 400
    
    response = es.search(index='logs', body={
        'query': {
            'match': {'entities': keyword}
        }
    })

    return jsonify(response['hits']['hits'])

if __name__ == '__main__':
    app.run(debug=True)
