class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost occurrence of target
        def findLeftmost():
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = s + (e - s) // 2
                if nums[mid] == target:
                    e = mid - 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return s
        
        # Helper function to find the rightmost occurrence of target
        def findRightmost():
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = s + (e - s) // 2
                if nums[mid] == target:
                    s = mid + 1
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return e
        
        leftmost = findLeftmost()
        rightmost = findRightmost()
        
        # If target is not found, return [-1, -1]
        if leftmost > rightmost:
            return [-1, -1]
        
        return [leftmost, rightmost]
