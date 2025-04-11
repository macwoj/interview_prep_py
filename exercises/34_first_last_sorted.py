
from typing import List

# Ologn space: O1
class Solution:
    def bin(self,nums,target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
    def binUpper(self,nums,target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1,-1]
        lo = self.bin(nums,target)
        if nums[lo] != target:
            return [-1,-1]
        hi = self.binUpper(nums,target)
        return [lo,hi]
    
# variant: find count of target
# Ologn space: O1
class Solution2:
    def bin(self,nums,target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
    def binUpper(self,nums,target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return 0
        lo = self.bin(nums,target)
        if nums[lo] != target:
            return 0
        hi = self.binUpper(nums,target)
        return hi-lo+1
    
#variant: find count of unique elements
# Oklogn k number of unique numbers
class Solution3:
    def countUnique(self,nums):
        result=0
        i=0
        while i<len(nums):
            target = nums[i]
            lo,hi=i,len(nums)-1
            while lo<=hi:
                mid = lo +(hi-lo)//2
                if nums[mid] <= target:
                    lo=mid+1
                else:
                    hi = mid-1
            result+=1
            i=hi+1
        return result

s = Solution2()
assert s.searchRange([2,2,3,3,3,9,9,9,9,9,10,12,12],9) == 5

s=Solution3()
assert s.countUnique([5,5,5,5,5,5,8,8,8,9,9,9,9,9,9,9,9,9]) == 3
assert s.countUnique([i for i in range(10)]) == 10