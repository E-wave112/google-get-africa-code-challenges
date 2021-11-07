from itertools import permutations
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        set_permute = list(set(list(permutations(nums))))
        list_permute = [list(i) for i in set_permute]
        return list_permute
        