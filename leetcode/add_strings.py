# import test cases
import unittest

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # create a numerical string to int mapping to convert the former to the latter without using built in functions
        int_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        num1_int = 0
        num2_int = 0
        for i in self.num1:
            num1_int = 10*num1_int + int_dict[i]

        for j in self.num2:
            num2_int = 10*num2_int + int_dict[j]

        return str(num1_int + num2_int)

soln = Solution()

class AddStringsTest(unittest.TestCase):
    def add_strings(self):
        self.assertEqual(soln.addStrings("1200","34"), "1234")
        self.assertEqual(soln.addStrings("274","181"), "455")
        self.assertEqual(soln.addStrings("215","806"), "1021")



if __name__ == '__main__':
    unittest.main()