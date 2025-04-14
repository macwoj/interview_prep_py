
import heapq
from typing import List

# Onlogk space Ok
def findKthLargest(nums: List[int], k: int) -> int:
    h=[]
    for n in nums:
        heapq.heappush(h,n)
        while len(h)>k:
            heapq.heappop(h)
    return h[0]

#variant: find k+1
# Onlogk space Ok
def findKthLargest2(nums: List[int], k: int) -> int:
    if k+1>len(nums):
        return 0
    k+=1
    h=[]
    for n in nums:
        heapq.heappush(h,n)
        while len(h)>k:
            heapq.heappop(h)
    return h[0]

#variant: k smallest
# Onlogk space Ok
def findKthSmallest(nums: List[int], k: int) -> int:
    h=[]
    for n in nums:
        heapq.heappush(h,-n)
        while len(h)>k:
            heapq.heappop(h)
    return -h[0]