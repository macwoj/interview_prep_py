

from typing import List

# Ologn space: O1
class Solution:
    def find(self,nums,k):
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            missing = nums[mid]-mid-1
            if missing < k:
                lo=mid+1
            else:
                hi=mid-1
        return lo+k

s=Solution()
print(s.find([1,2,3,4],3))

#variant LC1060, missing from the starting index
# Ologn space: O1

class Solution2:
    def missingElement(self, nums: List[int], k: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            target=nums[mid]-mid-nums[0]
            if target < k:
                lo=mid+1
            else:
                hi=mid-1
        return hi+k+nums[0]