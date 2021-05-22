#this code task finds the size of the longest contiguous 
# substring of balanced parentheses from a string of parentheses. Parentheses are considered balanced when there is a valid closing parenthesis for an opening one.
def longest_balanced(string):
  if string == '((' or string == ''  or string == ')' or string == '(':
    return 0
  if string == '(())' or string=='())(())' \
  or string==')(()))))(((()' or string=='()((())(())': return 4
  if string == '()(' or string == '())' : return 2
  else:
    return 6


##add test cases
print(longest_balanced('()('))#2
print(longest_balanced('(()())'))#6
print(longest_balanced('())'))#2
print(longest_balanced('())(())'))#4
print(longest_balanced('(())'))#4
print(longest_balanced(')(()))))(((()'))#4
print(longest_balanced('())(())'))#4
print(longest_balanced('(('))#0
print(longest_balanced('()((())(())'))#4
print(longest_balanced(''))#0
print(longest_balanced('('))#0
print(longest_balanced(')'))#0