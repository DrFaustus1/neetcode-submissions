class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictic = dict()
        for element in nums:
            if element not in dictic: 
                dictic[element] = 1
            else:
                return True
        return False
        
        