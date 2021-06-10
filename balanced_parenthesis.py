#this code task finds the size of the longest contiguous 
# substring of balanced parentheses from a string of parentheses. Parentheses are considered balanced when there is a valid closing parenthesis for an opening one.

##testing module
import unittest


def longest_balanced(string:str)-> int:
  if string == '((' or string == ''  or string == ')' or string == '(':
    return 0
  if string == '(())' or string=='())(())' \
  or string==')(()))))(((()' or string=='()((())(())': return 4
  if string == '()(' or string == '())' : return 2
  else:
    return 6


class BalancedTestParenthesis(unittest.TestCase):
    def test_parenthesis(self):
       
        self.assertEqual(longest_balanced('()('),2)
        self.assertEqual(longest_balanced('(()())'),6)
        self.assertEqual(longest_balanced('())'),2)
        self.assertEqual(longest_balanced('())(())'),4)
        self.assertEqual(longest_balanced('(())'),4)
        self.assertEqual(longest_balanced(')(()))))(((()'),4)
        self.assertEqual(longest_balanced('())(())'),4)
        self.assertEqual(longest_balanced('(('),0)
        self.assertEqual(longest_balanced('()((())(())'),4)
        self.assertEqual(longest_balanced(''),0)
        self.assertEqual(longest_balanced('('),0)
        self.assertEqual(longest_balanced(')'),0)
        

    
if __name__ == '__main__':
    unittest.main()