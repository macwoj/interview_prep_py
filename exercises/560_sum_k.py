
#clarify that there are -1 numbers
from collections import defaultdict
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    total = 0
    csum = defaultdict(int)
    csum[0] = 1
    result = 0
    for n in nums:
        total += n
        if total - k in csum:
            result += csum[total - k]
        csum[total] += 1
    return result

#variant: return True if there is an array
def subarraySum2(nums: List[int], k: int) -> int:
    total = 0
    csum = set()
    csum.add(0)
    for n in nums:
        total += n
        if total - k in csum:
            return True
        csum.add(total)
    return False

print(subarraySum2([1,1,1],2))#True
print(subarraySum2([1,4,7],3)) #False

#variant: only + numbers, return True/False
# move right and of sum>k move left to bring it down
def subarraySum3(nums: List[int], k: int) -> int:
    left=0
    total=0
    for right in range(len(nums)):
        total+=nums[right]
        while total>k:
            total-=nums[left]
            left+=1
        if total==k:
            return True
    return False



print(subarraySum3([1,1,1],2))#True
print(subarraySum3([1,4,7],3)) #False