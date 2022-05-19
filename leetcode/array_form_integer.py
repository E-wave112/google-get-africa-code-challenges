import unittest
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_num = int("".join([str(i) for i in num])) + k
        str_back = str(str_num)
        return [int(i) for i in str_back]


soln = Solution()


class ArrayTest(unittest.TestCase):
    def test_array_from(self):
        self.assertEqual(soln.addToArrayForm([1, 2, 0, 0], 34), [1, 2, 3, 4])
        self.assertEqual(soln.addToArrayForm([2, 7, 4], 181), [4, 5, 5])
        self.assertEqual(soln.addToArrayForm([2, 1, 5], 806), [1, 0, 2, 1])


if __name__ == "__main__":
    unittest.main()
