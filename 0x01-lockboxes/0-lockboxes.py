#!/usr/bin/python3
'''
Locked box challenge
'''


def canUnlockAll(boxes):
    '''
    Check boxes for key to unlock the next box
    '''
    if len(boxes[0]) == 0:
        return (False)
    visited = set([0])
    locked = set(boxes[0]).difference(set([0]))
    while len(locked) > 0:
        idx = locked.pop()
        if not idx or idx >= len(boxes) or idx < 0:
            continue
        if idx not in visited:
            locked = locked.union(boxes[idx])
            visited.add(idx)
    return len(boxes) == len(visited)