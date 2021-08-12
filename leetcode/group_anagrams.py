
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