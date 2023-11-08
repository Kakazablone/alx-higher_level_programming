#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys

status_codes = {}
total_size = 0
lines_read = 0

try:
    with sys.stdin as file:
        """Reading and parsing lines"""
        for line in file:
            line = line.split(" ")
            if line[-2] in status_codes:
                status_codes[line[-2]] += 1
            else:
                status_codes[line[-2]] = 1
            total_size += int(line[-1])
            lines_read += 1
            if lines_read % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_codes):
                    print("{}: {}".format(code, status_codes[code))
finally:
    print("File size:", total_size)
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code))
