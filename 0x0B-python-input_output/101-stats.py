#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys


def print_metrics(total_file_size, s_code_count):
    print("File size:", total_file_size)
    for code in sorted(s_code_count.keys()):
        if s_code_count[code] > 0:
            print("{}: {}".format(code, s_code_count[code]))


s_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0

try:
    line_count = 0
    for line in sys.stdin:
        line_toks = line.split()
        if len(line_toks) >= 8:
            status_code = int(line_toks[-2])
            file_size = int(line_toks[-1])
            total_file_size += file_size

            if status_code in s_code_count:
                s_code_count[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_file_size, s_code_count)

except KeyboardInterrupt:
    pass
finally:
    print_metrics(total_file_size, s_code_count)
