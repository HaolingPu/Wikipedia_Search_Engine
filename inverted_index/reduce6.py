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
    # print(f'{new_key}\t{doc_id} {term} {idf} {DF} {TF} {Norm}')
    term_dict = {}
    # { "happy" : [(a,b,c), (a,b,c), ()]}
    for line in group:
        new_key, doc_id, term, idf, DF, TF, Norm = line.strip().split()
        if term not in term_dict:
            term_dict[term] = []
        term_dict[term].append((doc_id, TF, Norm))

    for term, docs in term_dict.items():  #terms is key, docs is value (list)
        for doc_info in docs:
            print(f"{term} {idf}" + "\t".join(doc_info))


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()