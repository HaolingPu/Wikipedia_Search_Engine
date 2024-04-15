#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys
import itertools
import math

def reduce_one_group(key, group, N):
    """Reduce one group."""
    # print(f'{doc_id}\t{term} {DF} {TF}')

    for line in sys.stdin:
        doc_id, term, DF, TF = line.strip().split()
        idf = float(math.log10(N / float(DF)))
        # print("N*:", N)
        # print("DF*: ", DF)
        # print("log*: ", DF)
        # print("IDF*: ", math.log10(N / float(DF)))
        w = float(TF)*idf
        print(f'{doc_id}\t{term} {DF} {TF} {idf} {w}')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    N = 0
    with open('total_document_count.txt', 'r') as file:
        # Reads the first line and converts it to an integer
        N = int(file.readline().strip())
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group, N)


if __name__ == "__main__":
    main()
