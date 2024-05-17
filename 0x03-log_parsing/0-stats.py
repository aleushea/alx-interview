#!/usr/bin/python3
"""
This project is related to Python log parsing.
"""
import sys
import os


def print_data(total_file_size, status_code_data):
    """ This method prints total size and status code count """
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_code_data.items()):
        if count != 0:
            print('{}: {}'.format(code, count))

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_code_data = {code: 0 for code in status_codes}
total_file_size = 0
try:
    count = 0
    for line in sys.stdin:
        splitstr = line.split()
        try:
            total_file_size += int(splitstr[-1])
            code = splitstr[-2]
            if code in status_code_data:
                count += 1
                status_code_data[code] += 1
                if count % 10 == 0:
                    print_data(total_file_size, status_code_data)
        except:
            pass
except KeyboardInterrupt:
    print_data(total_file_size, status_code_data)
    raise
else:
    print_data(total_file_size, status_code_data)
    
