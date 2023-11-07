#!/usr/bin/python3

"""Reads from standard input and computes metrics.
Prints the following statistics after every ten lines or the input of a
keyboard interruption (CTRL + C):
    - Total file size so far
    - Count of read status codes so far."""


def print_stats(size, status_codez):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for key in sorted(status_codez):
        print("{}: {}".format(key, status_codez[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codez = {}
    compare_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codez)
                count = 1
            else:
                count += 1

            line_toks = line.split()

            try:
                file_size = int(line_toks[-1])
                size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = line_toks[-2]
                if status_code in compare_codes:
                    status_codez[status_code] = status_codez.get(status_code, 0) + 1
            except IndexError:
                pass

            print_stats(size, status_codez)

    except KeyboardInterrupt:
        print_stats(size, status_codez)
