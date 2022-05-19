import unittest


class Solution:
    def plusOne(self, digits):
        final = []
        list_str = [str(i) for i in digits]
        to_str = list(str(int("".join(list_str)) + 1))
        if "-" in to_str:
            new_to_str = to_str[1:]
            new_to_str[0] = f"-{new_to_str[0]}"
            final.extend([int(i) for i in new_to_str])
        else:
            final = [int(j) for j in to_str]
        return final


soln = Solution()

# run tests cases


class PlusOne(unittest.TestCase):
    def test_plus_one(self):
        self.assertEqual(soln.plusOne([1, 2, 1]), [1, 2, 2])
        self.assertEqual(soln.plusOne([8, 5, 2]), [8, 5, 3])
        self.assertEqual(soln.plusOne([-1, 6, 9]), [-1, 6, 8])


if __name__ == "__main__":
    unittest.main()
