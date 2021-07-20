import unittest

class Solution:
    def plusOne(self, digits):
        list_str = [str(i) for i in digits]
        to_str = list(str(int("".join(list_str)) + 1))
        return [int(j) for j in to_str]


soln = Solution()

# run tests cases
class PlusOne(unittest.TestCase):
    def plus_one_test(self):
        self.assertEqual(soln.plusOne([1,2,1]),[1,2,2])
        self.assertEqual(soln.plusOne([8,5,2]),[8,5,3])
        self.assertEqual(soln.plusOne([-1,6,9]),[-1,6,8])


if __name__ == "__main__":
    unittest.main()

    
