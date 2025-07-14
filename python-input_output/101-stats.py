#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""


import sys

def print_stats(total_size, status_codes):
    """Prints collected statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 7:
            continue

        # File size is last element
        try:
            size = int(parts[-1])
            total_size += size
        except ValueError:
            pass

        # Status code is second last
        code = parts[-2]
        if code in valid_codes:
            status_codes[code] = status_codes.get(code, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

# Final print in case less than 10 lines or no Ctrl+C
print_stats(total_size, status_codes)

