#!/usr/bin/python3
"""determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Function:  method that
    determines if all the boxes can be opened.
    boxes: is a list of lists
    Return: return false or true
    """
    lists_of_keys = [0]

    for open_keys in lists_of_keys:
        for key in boxes[open_keys]:
            if key < len(boxes) and key not in lists_of_keys:
                lists_of_keys.append(key)
    return len(lists_of_keys) == len(boxes)
