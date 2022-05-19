import unittest

import itertools
from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_arr = []
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if digits == "":
            return []
        for each in digits:
            digits_arr.append(letter_map[each])
        product_digits = list(product(*digits_arr))
        letter_combo = ["".join(item) for item in product_digits]
        return letter_combo


#  run test cases
soln = Solution()


class TestPhone(unittest.TestCase):
    def test_letter_combinations(self):
        self.assertEqual(
            soln.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(
            soln.letterCombinations("468"),
            [
                "gmt",
                "gmu",
                "gmv",
                "gnt",
                "gnu",
                "gnv",
                "got",
                "gou",
                "gov",
                "hmt",
                "hmu",
                "hmv",
                "hnt",
                "hnu",
                "hnv",
                "hot",
                "hou",
                "hov",
                "imt",
                "imu",
                "imv",
                "int",
                "inu",
                "inv",
                "iot",
                "iou",
                "iov",
            ],
        )
        self.assertEqual(soln.letterCombinations(""), [])


if __name__ == "__main__":
    unittest.main()
