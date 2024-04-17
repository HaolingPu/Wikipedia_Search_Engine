"""Following."""
import flask
import index.api
import re
import math
import os

inverted_index = {}
stopwords = set()
pagerank = {}

@index.app.route('/api/v1/')
def get_info():
    """Return a list of services available."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)

    
def clean_content(content):
    # Remove non-alphanumeric characters (excluding spaces)
    content = re.sub(r"[^a-zA-Z0-9 ]+", "", content)
    # Convert to lower case
    content = content.casefold()
    # Split into words and remove stopwords
    filtered_words = []
    for word in content.split():
        if word not in stopwords:
            filtered_words.append(word)
    return filtered_words


def parse_inverted_index_line(line):
    parts = line.split()
    term = parts[0]
    idf = float(parts[1])
    postings = []
    # Loop over the rest of the line with step 3 as each posting has 3 numbers (doc_id, tf, norm_factor)
    for i in range(2, len(parts), 3):
        doc_id = int(parts[i])
        tf = int(parts[i+1])
        norm_factor = float(parts[i+2])
        postings.append((doc_id, tf, norm_factor))
    return term, idf, postings


def load_index():
    # load inverted_index
    file_name = index.app.config['INDEX_PATH']
    file_path = os.path.join('index_server', 'index', 'inverted_index', file_name)
    with open(file_path, 'r') as file:
        for line in file:
            term, idf, postings = parse_inverted_index_line(line.strip())
            inverted_index[term] = {'idf': idf, 'postings': postings}
    # load stopword
    file_path = os.path.join('index_server', 'index', 'stopwords.txt')
    with open(file_path, 'r') as file:
        for word in file:
            stopwords.add(word.strip())
    # load pagerank
    file_path = os.path.join('index_server', 'index', 'pagerank.out')
    with open(file_path, 'r') as file:
        for line in file:
            doc_id, PR = line.strip().split(',')
            pagerank[int(doc_id)] = float(PR)
    return

@index.app.route('/api/v1/hits/')
def get_hits():
    """Handle query and Return hit info"""
    query = flask.request.args.get('q', '')
    weight = flask.request.args.get('w', default=0.5, type=float)
    query_terms = list(clean_content(query))

    #find doc intersection
    document_sets = []
    for term in query_terms:
        if term in inverted_index:
            postings = inverted_index[term]['postings']
            document_sets.append({doc_id for doc_id, _, _ in postings})
        else:
            context = {"hits" : []}
            return flask.jsonify(**context) 
    
    # Return the intersection of all document sets, which will contain only common documents
    result = set.intersection(*document_sets)
    
    # now we make sure everything in the query_terms are valid
    
    # caculate query score
    query_scores = []
    for term in query_terms:
        q_score = query_terms.count(term)* float(inverted_index[term]['idf'])
        query_scores.append(q_score)
             

    query_norm = sum(x*x for x in query_scores)

    # caculate document score
    score = {} # doc_id : score
    for doc_id in result:
        doc_score = []
        for term in query_terms:
            for posting in inverted_index[term]['postings']:
                if doc_id == posting[0]:
                    doc_score.append(posting[1]*inverted_index[term]['idf'])
                    doc_norm = posting[2]
        # doc product
        if len(doc_score) != len(query_scores):
            print("LENGTH INCONSISTENT, DOT PRODUCT")
        s = sum(x * y for x, y in zip(doc_score, query_scores))
        s = s/(math.sqrt(query_norm)*math.sqrt(doc_norm))
        score[doc_id] = s
    
    #caculate the score_w
    hits = [] # list of dictionary doc_id : score_w
    for doc_id in result:
        score_dict = {}
        score_dict['docid'] = doc_id
        score_dict['score'] = weight*pagerank[doc_id] + (1-weight)*score[doc_id]
        hits.append(score_dict)
    sorted_hits = sorted(hits, key=lambda x: x['score'], reverse = True)
    context = {"hits" : sorted_hits}
    print(context)
    return flask.jsonify(**context)     

    

