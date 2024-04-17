from flask import Flask, request, render_template
import requests
import threading
import heapq
import flask
import search

@search.app.route('/', methods=['GET'])
def get_search():
    query = flask.request.args.get('q', '')
    weight = flask.request.args.get('w', 0.5)
    if query:
        results = fetch_results(query, weight)
    else:
        results = []

    connection = search.model.get_db()
    for result in results:
        docid = int(result['docid'])
        cur = connection.execute(
                "SELECT * FROM Documents WHERE docid = ?",
                (docid, )
            ).fetchone()
        result["title"] = cur["title"]
        result["summary"] = cur["summary"]
        result["url"] = cur["url"]

    context = {"results" : results}
    # print(context)
    return flask.render_template('index.html', **context)


def fetch_from_server(url, query, weight, output):
    """ Fetch search results from a single index server. """
    full_url = f"{url}?q={query}&w={weight}"
    response = requests.get(full_url)
    if response.status_code == 200:
        output.extend(response.json()['hits'])


def fetch_results(query, weight):
    threads = []
    results = []
    # This list will store the results from each thread
    output = []

    # Start a thread for each API endpoint
    for url in search.app.config['SEARCH_INDEX_SEGMENT_API_URLS']:
        thread = threading.Thread(target=fetch_from_server, args=(url, query, weight, output))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Use heapq to merge results and sort by score
    results = list(heapq.nlargest(10, output, key=lambda x: x['score']))
    return results
