# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_width = 1
        this, nxt = [root], []
        while this:
            width = self.get_width(this)
            if width != -1:
                max_width = max(max_width, width)
            for child in this:
                if not child:
                    continue
                if child.left:
                    nxt.append(child.left)
                if child.right:
                    nxt.append(child.right)
                if not child.left:
                    nxt.append(None)
                if not child.right:
                    nxt.append(None)
            this = nxt
            nxt = []

    def get_width(self, lst):
        first, last = 0, len(lst) - 1
        width = 0
        for node in range(len(lst)):
            if lst[node]:
                first = node
                break
        for node in range(len(lst) - 1, 0, -1):
            if lst[node]:
                last = node
                break
        if first <= last:
            return last - first
        return -1
