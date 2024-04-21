#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    doc_id_set = set()
    group = list(group)
    for line in group:
        term, doc_id = line.strip().split()
        doc_id_set.add(doc_id)
    for line in group:
        term, doc_id = line.strip().split()
        print(f'{term} {doc_id}\t{len(doc_id_set)}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
