#!/usr/bin/python3
"""
main
"""

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_traingle(traingle):
    for row in traingle:
        print('[{}]'.format(','.join(str(x) for x in row)))

if __name__ == '__main__':
    print_traingle(pascal_triangle(5))