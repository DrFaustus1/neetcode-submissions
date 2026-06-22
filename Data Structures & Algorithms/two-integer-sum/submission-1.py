class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictic = dict()
        for i, n in enumerate(nums):
            dictic[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dictic and dictic[diff] != i:
                return [i, dictic[diff]]



[5, 5]

(0, 5)
(1, 5)
        


