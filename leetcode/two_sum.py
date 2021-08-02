# import the testing module and iteration tools
import unittest
from itertools import combinations
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        index_dict = dict()
        counter = -1
        for i in nums:
            counter += 1
            index_dict[counter] = i

        x = list(combinations(nums,2))
        z_list = [list(i) for i in x]
        z_sum = [i for i in z_list if sum(i) == target][0]
        print(z_sum)
        z_index = [keyss for keyss in index_dict.keys() if index_dict[keyss] in z_sum]
        return z_index

soln = Solution()

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(soln.two_sum([2,7,11,15],9),[0,1])
        self.assertEqual(soln.two_sum([3,2,4],6),[1,2])
        self.assertEqual(soln.two_sum([3,3],6),[0,1])


if __name__ == '__main__':
    unittest.main()