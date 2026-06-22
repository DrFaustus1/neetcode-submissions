class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix: list = [1]
        suffix: list = [1]
        for i in range(1, len(nums)):
            proizv = prefix[i-1] * nums[i-1]
            prefix.append(proizv)
        for i in range(len(nums)-2, -1, -1):
            proizv = suffix[0] * nums[i+1]
            suffix.insert(0, proizv)
        return [suffix[i] * prefix[i] for i in range(len(suffix))]
        