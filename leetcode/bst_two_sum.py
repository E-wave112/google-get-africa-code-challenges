from typing import Optional
import unittest

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
        res_filter = [i for i in res if i != None]
        total_root = list(combinations(res_filter, 2))
        for i in total_root:
            if sum(i) == k:
                return True
        return False


soln = Solution()

# run tests cases
class BstSum(unittest.TestCase):
    def test_bst_sum(self):
        self.assertEqual(soln.findTarget([5, 3, 6, 2, 4, None, 7], 28), False)
        self.assertEqual(soln.findTarget([2, 1, 3], 4), True)
        self.assertEqual(soln.findTarget([2, 1, 3], 1), False)
        self.assertEqual(soln.findTarget([2, 1, 3], 3), True)


if __name__ == "__main__":
    unittest.main()
