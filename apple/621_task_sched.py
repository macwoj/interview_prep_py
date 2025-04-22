from collections import defaultdict
import heapq
from typing import List


class Solution:

    # 1. frequency
    # 2. max heap
    # 3. pop from heap and decrease freq for each n+1, n+1 is the actual cycle length
    # 4. add to result the cycle count or if heap not empty the whole cycle n+1
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for x in tasks:
            freq[x]+=1
        h = [-v for k,v in freq.items()]
        heapq.heapify(h)
        result = 0
        # A B
        while h:
            tmp=[]
            cycle = 0
            while cycle<n+1 and h:
                cycle+=1
                top=-heapq.heappop(h)
                top-=1
                if top>0:
                    tmp.append(-top)
            for x in tmp:
                heapq.heappush(h,x)
            result+= n+1 if h else cycle

        return result