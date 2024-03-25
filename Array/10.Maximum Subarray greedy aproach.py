class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        overall_max = -inf
        for num in nums:
            current_max = max(current_max + num, num)
            overall_max = max(overall_max, current_max)
        return overall_max