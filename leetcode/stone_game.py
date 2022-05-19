import unittest
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex_throws = [i for i in piles if piles.index(i) % 2 == 0]
        lee_throws = [i for i in piles if piles.index(i) % 2 != 0]
        return alex_throws != lee_throws


soln = Solution()

# create test cases
class test_stone_game(unittest.TestCase):
    def test_stone(self):
        self.assertEqual(soln.stoneGame([5, 3, 4, 5]), True)
        self.assertEqual(soln.stoneGame([3, 9, 3, 7, 4, 5]), True)
        self.assertEqual(soln.stoneGame([6, 3, 4, 6]), True)


if __name__ == "__main__":
    unittest.main()
