#!/usr/bin/python3

"""
A script that reads stdin line by line and computes stats.
prints the statuscount
"""

import sys

if __name__ == "__main__":
    status_code = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0}

    line_count = 1
    total_file_size = 0

    def parse_log_line(log_line):
        # Read, parse, and get data
        try:
            parsed_line = log_line.split()
            code = parsed_line[-2]
            if code in status_code:
                status_code[code] += 1
            return int(parsed_line[-1])
        except Exception:
            return 0

    def print_statistics():
        # Print status in ascending order
        print("File size: {}".format(total_file_size))
        for key in sorted(status_code.keys()):
            if status_code[key]:
                print("{}: {}".format(key, status_code[key]))

    try:
        for line in sys.stdin:
            total_file_size += parse_log_line(line)
            if line_count % 10 == 0:
                print_statistics()
            line_count += 1
    except KeyboardInterrupt:
        print_statistics()
        raise
