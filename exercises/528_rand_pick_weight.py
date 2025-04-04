
from collections import defaultdict
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        pre = 0
        for n in w:
            pre+=n
            self.w.append(pre)

    def pickIndex(self) -> int:
        target = random.random()*self.w[-1]
        lo,hi=0,len(self.w)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if self.w[mid] < target:
                lo = mid + 1
            else:
                hi = mid-1
        return lo

s = Solution([1,3,2])

freq = defaultdict(int)
for i in range(100):
    freq[s.pickIndex()]+=1
print(freq)

#variant: city population
# input [["Seatle",500],["New York",900],["Los Angeles",400]]

class Solution2:

    def __init__(self, w):
        pre = 0
        self.w = []
        for city,pop in w:
            pre +=pop
            self.w.append((pre,city))
    def pickIndex(self):
        target = random.random()*self.w[-1][0]
        lo,hi=0,len(self.w)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.w[mid][0] < target:
                lo=mid+1
            else:
                hi=mid-1
        return self.w[lo][1]
    
s = Solution2([["Seatle",500],["New York",900],["Los Angeles",400]])

freq = defaultdict(int)
for i in range(1000):
    freq[s.pickIndex()]+=1
print(freq)