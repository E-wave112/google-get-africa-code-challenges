import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# run test cases
soln = Solution()

class Palindrome_test(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(soln.isPalindrome(-121),False)
        self.assertEqual(soln.isPalindrome(10),False)
        self.assertEqual(soln.isPalindrome(101),True)

if __name__ == "__main__":
    unittest.main()
