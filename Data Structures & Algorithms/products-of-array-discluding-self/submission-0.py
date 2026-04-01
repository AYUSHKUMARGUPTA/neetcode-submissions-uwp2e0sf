class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        rp = 1
        for i in range(n):
            result[i] = rp
            rp *= nums[i]
        rp = 1
        for i in reversed(range(n)):
            result[i] *= rp
            rp *= nums[i]
        return result