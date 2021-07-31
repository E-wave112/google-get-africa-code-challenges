# testing module
import unittest


singles = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

doubles = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens_num = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes_num = ('', 'Thousand', 'Million', 'Billion','Trillion','Quadrillion',
'Quintillion','Sextillion','Septillion','Octillion','Nonillion','Decillion',
'Undecillion','Duodecillion','Tredecillion','Quattuordecilllion','Quindecillion',
'Sexdecillion','Septendecillion','Octadecillion','Novemdecillion','Vingitillion')

def process(number:int, index:int):
    
    if number=='0':
        return 'Zero'
    
    length = len(number)
    
    if(length > 3):
        return False
    
    number = number.zfill(3)
    words = ''
 
    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])
    
    words += '' if number[0] == '0' else singles[hdigit]
    words += ' Hundred ' if not words == '' else ''
    
    if(tdigit > 1):
        words += tens_num[tdigit - 2]
        words += ' '
        words += singles[odigit]
    
    elif(tdigit == 1):
        words += doubles[(int(tdigit + odigit) % 10) - 1]
        
    elif(tdigit == 0):
        words += singles[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += suffixes_num[index]
        
    return words;
    
def convert_to_words(num):
    length = len(str(num))
    
    if length>20:
        return 'Maximum number limit exceeded !'
    
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []
 
    for i in range(length - 1, -1, -3):
        words.append(process(str(num)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;

    words_converted = ''
    for s in reversed(words):
        temp = s + ' '
        words_converted += temp
    
    return words_converted

# write test cases

class Num2WordsTest(unittest.TestCase):
    def test_num_words(self):
        self.assertEqual(convert_to_words(234),"two hundred thirty four")
        self.assertEqual(convert_to_words(3835217595),"three billion eight hundred thirty five million two hundred seventeen thousand five hundred ninety five")
        self.assertEqual(convert_to_words(19000000001),"nineteen billion one")


if __name__ == '__main__':
    unittest.main()
