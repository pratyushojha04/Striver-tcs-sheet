class Solution:
    def firstMissingPositive(self, nums):
        nums_set = set(nums)
        i = 1
        while i in nums_set:
            i += 1
        return i
s=Solution()
print(s.firstMissingPositive([3,4,-1,1]))