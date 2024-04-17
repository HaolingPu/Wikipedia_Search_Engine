"""Following."""
import flask
import index.api
import re
import math




            

def clean_content(content):
    stopwords = set()
    with open('stopwords.txt', 'r') as file:
        for word in file:
            stopwords.add(word.strip())
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

@index.app.route('/api/v1/')
def get_info():
    """Return a list of services available."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return flask.jsonify(**context)

@index.app.route('/api/v1/hits/')
def load_index():
    """Handle query and Return hit info"""
    query = flask.request.args.get('q', '')
    weight = flask.request.args.get('w', default=0.5, type=float)
    query = list(clean_content(query))
    index_path = index.app.config['INDEX_PATH']
    sets = []
    doc_dict = {}  # key [doc_id, word], value = [tf, norm]
    idf_dict = {} # key [word], value = [idf]
    
    # match: [happy: [doc1, doc3, doc4], sad: [doc1, doc2, doc4]]
    # [doc1, doc3, doc4] intersect with [doc1, doc2, doc4] = [doc1, doc4]
    # if query doesn't appear # 
    
    with open(index_path, 'r') as file:
        # each line is a unique word among all documents
        for line in file:
            term = line.strip().split()[0]
            idf_dict[term] = float(line.strip().split()[1])
            if term in query:
                # extract all documents for this particular word and put them into a set, append to sets
                parts = line.strip().split()
                postings = []                 
                for i in range(2, len(parts), 3):
                    doc_id = int(parts[i])
                    # tf, norm
                    doc_dict[(doc_id, term)] = [int(parts[i+1]), float(parts[i+2])]
                    postings.append(doc_id)
                sets.append(set(postings))
    if sets is not None:
        result = set.intersection(*sets)
    
    # caculate query score
    query_score = []
    for term in query:
        query_score = query.count(term)*idf_dict[term]
        query_score.append(query_score)
    query_norm = sum(x*x for x in query_score)

    # caculate document score
    score = {} # doc_id : score
    for doc_id in result:
        doc_score = []
        for term in query:
            doc_score.append(doc_dict[(doc_id, term)][0]*idf_dict[term])
            doc_norm = doc_dict[(doc_id, term)][1]
        # doc product
        if len(doc_score) != len(query_score):
            print("LENGTH INCONSISTENT, DOT PRODUCT")
        s = sum(x * y for x, y in zip(doc_score, query_score))
        s = s/(math.sqrt(query_norm)*math.sqrt(doc_norm))
        score[doc_id] = s
    
    #caculate the score_w
    hits = [] # list of dictionary doc_id : score_w
    with open('pagerank.out', 'r') as file:
        for line in file:
            doc_id, PR = line.strip().split()
            PR = float(PR)
            if doc_id in result:
                score_dict = {}
                score_dict['docid'] = doc_id
                score_dict['score'] = weight*PR + (1-weight)*score[doc_id]
                hits.append(score_dict)

    context = {"hits" : hits}
    return flask.jsonify(**context)     

    

