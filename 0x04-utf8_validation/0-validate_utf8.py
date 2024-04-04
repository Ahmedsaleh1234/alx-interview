#!/usr/bin/env python3
"""0. UTF-8 Validation"""


def count_bits(n):
    """count the frist bits eqaul to one in byte"""
    count = 0
    j = 1 << 7
    while n & j:
        j >>= 1
        count += 1
    return count


def validUTF8(data):
    """
    Function: that determines if a given data set
    represents a valid UTF-8 encoding
    @data: that will be check
    Return: True if encoded by utf-8 False atherwise
    """
    count = 0
    for i in range(len(data)):
        if count == 0:
            count = count_bits(data[i])
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not ((data[i] & 1 << 7) and not (data[i] & 1 << 6)):
                return False
        count -= 1
    return True
