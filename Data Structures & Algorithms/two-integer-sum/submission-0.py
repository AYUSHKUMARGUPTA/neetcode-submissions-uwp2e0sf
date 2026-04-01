class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i, n in enumerate(nums):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            seen[n] = i