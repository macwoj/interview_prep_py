

from collections import Counter, defaultdict
import random
from typing import List

# On space: On
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for i in range(len(nums)):
            self.nums[nums[i]].append(i)

    def pick(self, target: int) -> int:
        ra = random.random()
        i = int(ra * len(self.nums[target]))
        return self.nums[target][i]
    
#variant: pick k numbers, cannot pick number twice, return as integer array, no extra space complexity, On runtime
# reservoir sampling
# On space O1

def sample(nums,k):
    result = nums[:k]
    for i in range(k,len(nums)):
        n = random.randint(0,i) # 0 and i inclusive
        # print(f'{i} {n}')
        if n < k:
            result[n]=nums[i]
    return result

print(sample([6,8,2,1,3,10,4],3))

# variant: rand output index of max, On space O1

def sample(nums):
    max_num = float('-inf')
    index = -1
    n = 0
    for i,v in enumerate(nums):
        if v < max_num:
            continue
        elif v>max_num:
            max_num=v
            index=i
            n=0
        else:
            n+=1
            if random.randint(0,n) == 0:
                index=i
    return index

print(sample([11,11,2,30,6,30,30,2,62,62]))
print(sample([11,11,2,30,6,30,30,2,29,29]))
print(sample([1,1,1,1,1]))

print(Counter([sample([11,11,2,30,6,30,30,2,62,62]) for _ in range(100000)]))
print(Counter([sample([11,11,2,30,6,30,30,2,29,29]) for _ in range(100000)]))
print(Counter([sample([1,1,1,1,1]) for _ in range(100000)]))
