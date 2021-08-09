class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # create a numerical string to int mappinng to convert the former to the latter without using built in functions
        int_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        num1_int = 0
        num2_int = 0
        for i in num1:
            num1_int = 10*num1_int + int_dict[i]

        for j in num2:
            num2_int = 10*num2_int + int_dict[j]

        return str(num1_int + num2_int)