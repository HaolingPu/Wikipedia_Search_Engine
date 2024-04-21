#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys

total_doc = 0
for line in sys.stdin:
    total_doc += 1

print(total_doc)
