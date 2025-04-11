
from typing import List

# On storage: O1
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower,upper]]
        result = []
        if lower < nums[0]:
            result.append([lower,nums[0]-1])
        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i]>1:
                result.append([nums[i]+1,nums[i+1]-1])
        if upper>nums[-1]:
            result.append([nums[-1]+1,upper])
        return result
    
#variant: formatting, more than 3 missing 'n-m', one number individual string, 2 missing push them individually
class Solution2:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        nums.append(upper+1) ## HERE
        curr = lower
        for n in nums:
            if n-curr>2:
                result.append(f'{curr}-{n-1}')
            elif n-curr>1:
                result.append(str(curr))
                result.append(str(n-1))
            elif n-curr==1:
                result.append(str(curr))
            curr=n+1
        print(result)
        return result

s = Solution2()
assert s.findMissingRanges([5, 8, 9, 15, 16, 18, 20],2,87) == ["2-4", "6", "7", "10-14", "17", "19", "21-87"]