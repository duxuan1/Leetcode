from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, this, next = [root.val], [root], []
        while this:
            for node in this:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if next:
                res.append(next[-1].val)
            this = next
            next = []
        return res
