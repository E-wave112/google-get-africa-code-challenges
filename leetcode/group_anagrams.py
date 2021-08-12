
from collections import defaultdict
 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initializing list
        # test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum'] [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
        # test_list = ["eat","tea","tan","ate","nat","bat"] [["bat"],["nat","tan"],["ate","eat","tea"]]
        # test_list = ["a"] [["a"]]
        # test_list = [""] [[""]]
        temp = defaultdict(list)
        for ele in test_list:
            temp[str(sorted(ele))].append(ele)
            # print(temp)
        res = list(temp.values())
        return res