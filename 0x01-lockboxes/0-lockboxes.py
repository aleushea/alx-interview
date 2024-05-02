#!/usr/bin/python3

def canUnlockAll(boxes):
    """
        Parameter: boxes
        Return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False
    unlocked = [0]
    for x in unlocked:
        for y in boxes[x]:
            if y not in unlocked and y < len(boxes):
                unlocked.append(y)
    return len(unlocked) == len(boxes)
