# import the unittest module
import unittest


def find_alphabet(words):
    if len(words) == 0:
        return []
    # check if a letter of a word is in the alphabet
    # get a list of all letters in the alphabet both lower and upper case
    present_alphabets = []
    upper_case_alphabet = [chr(i) for i in range(65, 91)]
    lower_case_alphabet = [chr(i) for i in range(97, 123)]
    # merge the above lists
    alphabet = upper_case_alphabet + lower_case_alphabet
    # sort the words list in alphabetical order
    sorted_word = sorted(words)
    sorted_words = [i for i in sorted_word]
    # check if each word contains a letter from the alphabet
    for word in sorted_words:
        for letter in word:
            if letter in alphabet:
                present_alphabets.append(letter)

    # convert to a set to get the unique alphabets and then back to a list and sort
    present_unique_alphas = sorted(list(set(present_alphabets)))
    # return the alphabet with the letters that are present in the words iteratively
    return [i for i in present_unique_alphas]


# this function reuses part of the first function to compute all possible alphabets that can be formed from a given dictionary
def find_all_alphabets(words):
    initial_alphabets = find_alphabet(words)
    all_possible_alphabets = [
        i.upper() if i.islower() else i.lower() for i in initial_alphabets
    ]
    final = initial_alphabets + all_possible_alphabets
    final.sort()
    return [i for i in final]


# write test cases
class TestFindAlphabet(unittest.TestCase):
    # write a function to for five test cases
    def test_find_alphabet(self):
        self.assertEqual(
            find_alphabet(["ART", "RAT", "CAT", "CAR"]), ["A", "C", "R", "T"]
        )
        self.assertEqual(find_alphabet(["a", "bbl", "bba"]), ["a", "b", "l"])
        self.assertEqual(
            find_alphabet(["zal", "zb", "zzlb", "zzz"]), ["a", "b", "l", "z"]
        )
        self.assertEqual(find_alphabet(["aBa", "aaa", "bB", "bbB"]), ["B", "a", "b"])
        self.assertEqual(find_alphabet([]), [])


# write test cases for the find_all_alphabets function
class TestFindAllAlphabets(unittest.TestCase):
    # write a function to for five test cases
    def test_find_all_alphabets(self):
        self.assertEqual(
            find_all_alphabets(["ART", "RAT", "CAT", "CAR"]),
            ["A", "C", "R", "T", "a", "c", "r", "t"],
        )
        self.assertEqual(
            find_all_alphabets(["a", "bbl", "bba"]), ["A", "B", "L", "a", "b", "l"]
        )
        self.assertEqual(
            find_all_alphabets(["zal", "zb", "zzlb", "zzz"]),
            ["A", "B", "L", "Z", "a", "b", "l", "z"],
        )
        self.assertEqual(
            find_all_alphabets(["aBa", "aaa", "bB", "bbB"]),
            ["A", "B", "B", "a", "b", "b"],
        )
        self.assertEqual(find_all_alphabets([]), [])


if __name__ == "__main__":
    unittest.main()
