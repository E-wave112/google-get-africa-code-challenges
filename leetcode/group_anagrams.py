# import the testing module
import unittest
from typing import List
from collections import defaultdict
 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initializing list
        # test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum'] [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
        # test_list = ["eat","tea","tan","ate","nat","bat"] [["bat"],["nat","tan"],["ate","eat","tea"]]
        # test_list = ["a"] [["a"]]
        # test_list = [""] [[""]]
        # using the defaultdict library
        temp_dict = defaultdict(list)
        for item in strs:
            temp_dict[str(sorted(item))].append(item)
            # print(temp)
        res = list(temp_dict.values())
        return res

soln = Solution()
class anagramsTest(unittest.TestCase):
    def group_anagrams(self):
        self.assertEqual(soln.groupAnagrams(['lump', 'eat',  'me',  'tea', 'em', 'plum']),[['me', 'em'], ['lump', 'plum'], ['eat', 'tea']])
        self.assertEqual(soln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]),[["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(soln.groupAnagrams(["a"]),[["a"]])
        self.assertEqual(soln.groupAnagrams([""]),[[""]])

if __name__ == "__main__":
    unittest.main()
