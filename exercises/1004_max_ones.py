
# On storage: O1
from typing import List


def longestOnes(self, nums: List[int], k: int) -> int:
    if not nums:
        return 0
    result = 0
    flips = 0
    j = i = 0
    while i < len(nums):
        if nums[i] == 0:
            flips += 1
        while j<=i and flips > k:
            if nums[j] == 0:
                flips -= 1
            j += 1
        result = max(result,i-j+1)
        i += 1
    return result

#variant: Given an array days of 'W' and 'H' where 'W'  work day and 'H' a holiday, return the longest possible vacation with pto count
# On space O1
def vacation(days,pto):
    j=0
    result=0
    for i,v in enumerate(days):
        if v=='W':
            pto-=1
        while pto<0:
            if (days[j]=='W'):
                pto+=1
            j+=1
        result = max(result,i-j+1)

    return result


print(vacation(["W", "H", "W", "H", "W", "H", "W"],2)) # 5
print(vacation(["W", "W", "W", "H", "H", "W"],0)) # 2

#variant: given array of bools
def vacation(year,pto):
    j=0
    result=0
    for i,v in enumerate(year):
        if not v:
            pto-=1
        while pto<0:
            if (not year[j]):
                pto+=1
            j+=1
        result = max(result,i-j+1)

    return result