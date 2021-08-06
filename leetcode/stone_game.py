class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex_throws = [i for i in piles if piles.index(i) % 2 == 0]
        lee_throws = [i for i in piles if piles.index(i) % 2 != 0]
        return alex_throws != lee_throws