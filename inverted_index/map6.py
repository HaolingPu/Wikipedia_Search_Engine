#!/usr/bin/env python3
"""Map 6."""
import sys

#print(f'{doc_id}\t{term} {idf} {DF} {TF} {Norm}')
for line in sys.stdin:
    doc_id, term, idf, DF, TF, Norm = line.strip().split()
    new_key = doc_id % 3
    print(f'{new_key}\t{doc_id} {term} {idf} {DF} {TF} {Norm}')