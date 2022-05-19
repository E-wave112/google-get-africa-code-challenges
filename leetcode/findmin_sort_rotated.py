import unittest
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


soln = Solution()


class TestMin(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(soln.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(soln.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(soln.findMin([11, 13, 15, 17]), 11)


if __name__ == "__main__":
    unittest.main()
