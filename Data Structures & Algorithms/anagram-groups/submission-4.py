class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = dict()
        for word in strs:
            normalized = sorted(word)
            normalized_str = ''.join(normalized)
            if normalized_str not in dict1:
                dict1[normalized_str] = [word]
            else:
                dict1[normalized_str].append(word)
        return list(dict1.values())