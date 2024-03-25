import collections
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        l = []
        for i in c:
            if c[i] == 2:
                l.append(i)
        return l
s=Solution()
print(s.findDuplicates([4,3,4,5,1,2,1]))