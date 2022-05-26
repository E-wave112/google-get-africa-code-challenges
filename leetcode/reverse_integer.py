import unittest


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x_rev = 0
        if x > 0:
            x_rev = int(str(x)[::-1])
        elif x < 0:
            x_rev = int("-" + str(x)[::-1][:-1])

        return x_rev if x_rev in range(-(2**31), 2**31 - 1) else 0


soln = Solution()


class ReverseIntegerTest(unittest.TestCase):
    def test_normal_reverse_integer(self):
        self.assertEqual(soln.reverse(321), 123)

    def test_zero_case_reverse(self):
        self.assertEqual(soln.reverse(120), 21)

    def test_total_zero(self):
        self.assertEqual(soln.reverse(0), 0)

    def test_negative_case(self):
        self.assertEqual(soln.reverse(-321), -123)

    def test_numerical_limit_range(self):
        self.assertEqual(soln.reverse(2147483648), 0)


if __name__ == "__main__":
    unittest.main()
