##import test case module
import unittest


class Solution:
    def reverse(self, x: int) -> int:
        final = ''
        if x == 0:return 0
        elif x % 10 != 0 and x > 0 :
            final = int(str(x)[::-1])
        elif len(str(x)) == 1:final = x
        elif x < 0:final = int(f'-{str(abs(x))[::-1]}')
        elif x % 10 == 0 and x > 0:
            final = int(str(x).strip('0')[::-1])
        elif x % 10 == 0 and x < 0:
            y = str(abs(x))
            y_str =y.strip('0')[::-1]
            final = int(f'-{y_str}')
        if final not in range(-2**31,2**31+1):
            final = 0
        return final

# class ReverseIntegerTest(unittest.TestCase):
#     def test_reverse_integer(self):
