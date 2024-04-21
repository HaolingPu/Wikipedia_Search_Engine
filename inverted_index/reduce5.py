#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import math


def reduce_one_group(key, group):
    """Reduce one group, one document."""
    group = list(group)
    # print(f'{doc_id}\t{term} {DF} {TF} {idf} {w}')
    Norm = 0
    for line in group:
        doc_id, term, DF, TF, idf, w = line.strip().split()
        Norm += float(w)*float(w)
        # print("Current sum*: ", Sum)
    # print("Norm*: ", Norm)
    for line in group:
        doc_id, term, DF, TF, idf, _ = line.strip().split()
        print(f'{doc_id}\t{term} {idf} {DF} {TF} {Norm}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
