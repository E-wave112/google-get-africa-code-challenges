from typing import Optional
# Definition for a binary tree node.
from itertools import combinations
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque(root)
        while q:
            current = q.pop(0)
            yield current.value if current else None
            if current and not current.val:
                q.extend([current.left, current.right])
        
        res = list(q)
        res_filter = [i for i in res if i !== None]
        total_root = list(combinations(res_filter,2))
        for i in sum_root:
            if sum(i) == k: return True
        return False

       