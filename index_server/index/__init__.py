# ...
import flask
import os

app = flask.Flask(__name__)   # pylint: disable=invalid-name
app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")
import index.api  # noqa: E402  pylint: disable=wrong-import-position

# Load inverted index, stopwords, and pagerank into memory
index.api.load_index()


