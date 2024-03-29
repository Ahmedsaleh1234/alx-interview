#!/usr/bin/python3
""" 0x03. Log Parsing"""
import sys
import re
def main():
    """main"""
    i = 0
    size = 0
    status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    pattern =  r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET \/projects\/260 HTTP\/1\.1" \d{3} \d+'
    def print_log(fileSize, status_code):
        """print"""
        print("File size: {:d}".format(fileSize))
        for key in sorted(status_code.keys()):
            if status_code[key] != 0:
                print("{}: {:d}".format(key, status[key]))


    
    for line in sys.stdin:
        if (re.match(pattern, line)):
            words = line.split()
            if words[-2] in status_code.keys():
                status_code[words[-2]] += 1
            size += words[-1]
            



