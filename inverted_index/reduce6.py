#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import math


def reduce_one_group(key, group):
    """Reduce one group, one final partition %3."""
    group = list(group)
    # print(key)
    # print(f'{new_key}\t{doc_id} {term} {idf} {DF} {TF} {Norm}')
    term_dict = {}
    # { "happy" : [(a,b,c), (a,b,c), ()]}
    for line in group:
        new_key, doc_id, term, idf, DF, TF, Norm = line.strip().split()
        
        if term not in term_dict:
            term_dict[term] = []
        term_dict[term].append((idf, doc_id, TF, Norm))
    # sort by term 
    for term, docs in sorted(term_dict.items()):  #terms is key, docs is value (list)
        idf = docs[0][0]  # Take IDF from the first entry
        term_info = f"{term} {idf}"
        # for doc_info in sorted(docs, key=lambda x: x[1]):
        # idf, doc_id, TF, Norm = doc_info
        doc_info_strings = [f"{doc_id} {TF} {Norm}" for _, doc_id, TF, Norm in sorted(docs, key=lambda x: x[1])]
        print(f"{term_info} {' '.join(doc_info_strings)}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()