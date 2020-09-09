from typing import List, Set

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 1
        this, nxt = [root], []
        while this:
            for child in this:
                if child.children:
                    nxt.append(child.children)
            if not nxt: return depth
            this = nxt
            nxt = []
            depth += 1
