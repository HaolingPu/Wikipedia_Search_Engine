#!/usr/bin/env python3
"""Reduce 1."""
import sys
import re

stopwords = set()
with open('stopwords.txt', 'r') as file:
    for word in file:
        stopwords.add(word.strip())


def clean_content(content):
    """Clean content."""
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


for line in sys.stdin:
    doc_id, content = line.strip().split('\t', 1)
    # Clean and process the content
    clean_terms = clean_content(content)
    # Emit terms along with their document ID
    for term in clean_terms:
        # Use a set to emit each term only once per document
        print(f'{term}\t{doc_id}')
