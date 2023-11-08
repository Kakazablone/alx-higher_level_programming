#!/usr/bin/python3

"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
- Total file size up to that point.
- Count of read status codes up to that point.
"""

import sys

# Initialize variables to store metrics
total_size = 0
s_codecount = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    print(f"File size: {total_size}")

    # Print number of lines by status code in ascending order
    for status_code in sorted(s_codecount):
        count = s_codecount[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


try:
    for line in sys.stdin:
        # Split the input line and extract the status code and file size
        line_toks = line.split()
        if len(line_toks) >= 8:
            status_code = int(line_toks[-2])
            file_size = int(line_toks[-1])

            # Update total file size and status code counts
            total_size += file_size
            if status_code in s_codecount:
                s_codecount[status_code] += 1

            # Increment line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()
except KeyboardInterrupt:
    print_statistics()
