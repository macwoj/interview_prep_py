

from collections import defaultdict
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    sums = {}
    for i,v in enumerate(nums):
        tmp = target-v
        if tmp in sums:
            return [sums[tmp],i]
        sums[v] = i
    return []


#variant: return true if complement found, else return false
def twoSum2(nums: List[int], target: int) -> List[int]:
    sums = set()
    for v in nums:
        tmp = target-v
        if tmp in sums:
            return True
        sums.add(v)
    return False

#variant: dominoes 
# [[3, 4], [1, 9], [3, 4], [2, 1], [9, 1], [9, 1], [7, 6], [1, 9]]
# a1+b1 = target and a2+b2=target

def twoSum3(nums, target):
    dom = defaultdict(int)
    result = 0
    for d in nums:
        c = (target-d[0],target-d[1])
        if c in dom:
            result+=dom[c]
        dom[tuple(d)]+=1
    return result

print(twoSum3([[3, 4], [1, 9], [3, 4], [2, 1], [9, 1], [9, 1], [7, 6], [1, 9]],10))
print(twoSum3([[0,0],[0,0],[0,0],[0,0],[0,0]],0))