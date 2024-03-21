class Solution:
    def majorityElement(self, nums):
        n = len(nums)  
        counts = {}  
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for key, value in counts.items():
            if value >= n:  
                print( key ) 

s=Solution()
s.majorityElement([2,3,2])