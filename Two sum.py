class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]