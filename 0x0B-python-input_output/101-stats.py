#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys

codes = {}
size = 0
count = 0


try:
    for line in sys.stdin:
        line_toks = line.split(" ")
        code = line_toks[-2]
        if code in codes:
            codes[code] += 1
        else:
            codes[code] = 1
        size += int(line_toks[-1])
        count += 1
        if count % 10 == 0:
            print("Size:", size)
            for code in sorted(codes.keys()):
                print("{}: {}".format(code, codes[code]))
finally:
    print("Size:", size)
    for code in sorted(codes.keys()):
        print("{}: {}".format(code, codes[code]))
