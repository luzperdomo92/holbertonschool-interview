#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened """

    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    key = [0]
    for array in key:
        for elem in boxes[array]:
            if elem not in key and elem != array and elem < len(boxes) and elem != 0:
                key.append(elem)
    if len(key) == len(boxes):
        return True
    else:
        return False
