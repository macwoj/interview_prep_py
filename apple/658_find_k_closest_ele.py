
from typing import List


class Solution:
    # 1 bin search to find the insertion point
    # 2 find the rightindex on each iter with min diff
    # expand 2 pointers out from that point
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >len(arr):
            return []
        lo,hi=0,len(arr)-1
        idx,diff=0,abs(x-arr[0])
        while lo<=hi:
            mid=lo+(hi-lo)//2
            curr = abs(arr[mid]-x)
            if curr<diff or (curr==diff and arr[mid]<arr[idx]):
                idx,diff=mid,curr
            if arr[mid]==x:
                break
            elif arr[mid]<x:
                lo=mid+1
            else:
                hi=mid-1
        left=right=idx
        for i in range(k-1):
            if left==0:
                right+=1
            elif right==len(arr)-1 or abs(arr[left-1]-x) <= abs(arr[right+1]-x):
                left-=1
            else:
                right+=1
        return arr[left:right+1]