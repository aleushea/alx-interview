#!/usr/bin/python3

"""Log parsing"""

import sys

STATUS_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']
STATUS_CODE_DATA = {code: 0 for code in STATUS_CODES}
TOTAL_FILE_SIZE = 0
COUNT = 0


def print_data():
    """Prints total size and status code count."""
    print(f'File size: {TOTAL_FILE_SIZE}')
    for code, count in sorted(STATUS_CODE_DATA.items()):
        if count != 0:
            print(f'{code}: {count}')


try:
    for line in sys.stdin:
        parts = line.split()
        try:
            TOTAL_FILE_SIZE += int(parts[-1])
            code = parts[-2]
            if code in STATUS_CODE_DATA:
                COUNT += 1
                STATUS_CODE_DATA[code] += 1
                if COUNT % 10 == 0:
                    print_data()
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    print_data()
    raise
else:
    print_data()