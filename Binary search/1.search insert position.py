class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        start = 0
        end = n-1
        while(start <= end):
            mid = end+(start - end)//2
            if target > nums[mid]:
                start  = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        return start 
s=Solution()
s.searchInsert([1,3,5,6] ,5)

        