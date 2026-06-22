class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()
        for element in s:
            if element not in dict_s: 
                dict_s[element] = 1
            else:
                dict_s[element] += 1 
        for element in t:
            if element not in dict_t: 
                dict_t[element] = 1
            else:
                dict_t[element] += 1 
        return dict_s == dict_t

        