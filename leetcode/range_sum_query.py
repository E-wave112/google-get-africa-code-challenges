import unittest
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        list_sum = self.nums[left : right + 1]
        return sum(list_sum)


new_array = NumArray([-2, 0, 3, -5, 2, -1])


class NumArrayTest(unittest.TestCase):
    def test_num_array(self):
        self.assertEqual(new_array.sumRange(0, 2), 1)
        self.assertEqual(new_array.sumRange(2, 5), -1)
        self.assertEqual(new_array.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
