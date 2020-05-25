from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, this_level, next_level = [[root.val]], [root], []
        while this_level:
            sub = []
            for node in this_level:
                if node.left:
                    next_level.append(node.left)
                    sub.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    sub.append(node.right.val)
            if sub: res.append(sub)
            this_level = next_level
            next_level = []
        return res
