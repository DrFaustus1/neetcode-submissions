class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        sort_dict = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sort_dict[:k]]