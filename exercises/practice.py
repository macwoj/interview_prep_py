from collections import Counter
import random


class Solution:
    def __init__(self,cities):
        self.cities = cities
        self.sum = []
        s=0
        for city,pop in cities:
            s+=pop
            self.sum.append(s)

    def pickIndex(self):
        target = random.random()*self.sum[-1]
        lo,hi=0,len(self.sum)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.sum[mid]<target:
                lo=mid+1
            else:
                hi=mid-1
        return self.cities[lo][0]

s=Solution([["Seatle",500],["New York",900],["Los Angeles",400]])
print(Counter([s.pickIndex() for x in range(10000)]))