from itertools import combinations
from collections import Counter
from typing import List


class Solution:
    def filters(self, nums: List[int], target: int):
        return sum(nums) == target

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sum_combo = combinations(nums, 4)
        sum_combo_list = [sorted(list(item)) for item in sum_combo]
        sub_combo = [i for i in sum_combo_list if self.filters(i, target)]
        return [list(i) for i in set(map(tuple, sub_combo))]
