import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(node)
        on = True
        off = False

        while q:
            on, off = off, on
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if on:
                    level.reverse()
                res.append(level)
        return res
