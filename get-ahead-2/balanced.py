import re

def balanced_parenthesis(s):
    '''
    this finds the size of the longest contiguous substring of balanced parentheses. Parentheses are considered balanced when there is a valid closing parenthesis for nn opening one.
    '''
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == '(' and s[1] == ')':return 2

    if s == "((" or s == "))":
        return 0
    
    v = max([s.count(i) for i in s])
    pattern = f"(\({{1,{v}}})(\){{1,{v}}})"
    pattern_comp = re.compile(pattern)
    match = re.findall(pattern_comp,s)
    match_list = [''.join(i) for i in match]
    print(match_list)
    match_even = [len(i) for i in match_list if len(i) % 2 == 0]
    print(match_even)
    return max(match_even)


print(balanced_parenthesis('('))