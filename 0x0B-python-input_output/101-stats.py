#!/usr/bin/python3
"""
 Log parsing
"""
import sys


def print_stats(file_size, status_code_counts):
    """
    A script that reads stdin line by line and computes metrics:
    """
    print("File size: {}".format(file_size))
    for key in sorted(status_code_counts):
        print("{}: {}".format(key, status_code_counts[key]))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_code_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(file_size, status_code_counts)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    x = status_code_counts.get(line[-2], 0) + 1
                    status_code_counts[line[-2]] = x
            except IndexError:
                pass

        print_stats(file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_code_counts)
        raise
