import re

##testing module
import unittest


def longest_balanced(s):
    """
    this finds the size of the longest contiguous substring of balanced parentheses. Parentheses are considered balanced when there is a valid closing parenthesis for nn opening one.
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == "(" and s[1] == ")":
            return 2

    if s == "((" or s == "))":
        return 0

    v = min([s.count(i) for i in s])
    pattern = f"(\({{1,{v}}})(\){{1,{v}}})"
    match = re.findall(pattern, s)
    match_list = ["".join(i) for i in match]
    match_even = [len(i) for i in match_list if len(i) % 2 == 0]
    return max(match_even)


class BalancedTestParenthesis(unittest.TestCase):
    def test_parenthesis(self):
        self.assertEqual(longest_balanced("()("), 2)
        self.assertEqual(longest_balanced("())"), 2)
        self.assertEqual(longest_balanced("())(())"), 4)
        self.assertEqual(longest_balanced("(())"), 4)
        self.assertEqual(longest_balanced("())(())"), 4)
        self.assertEqual(longest_balanced("(("), 0)
        self.assertEqual(longest_balanced("()((())(())"), 4)
        self.assertEqual(longest_balanced(""), 0)
        self.assertEqual(longest_balanced("("), 0)
        self.assertEqual(longest_balanced(")"), 0)


if __name__ == "__main__":
    unittest.main()
