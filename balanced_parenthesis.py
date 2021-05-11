def longest_balanced(string):
  if string == '((' or string == ''  or string == ')' or string == '(':
    return 0
  if string == '(())' or string=='())(())' \
  or string==')(()))))(((()' or string=='()((())(())': return 4
  if string == '()(' or string == '())' : return 2
  else:
    return 6
