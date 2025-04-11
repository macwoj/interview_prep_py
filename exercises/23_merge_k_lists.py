import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#nlogk space Ok
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self,other: self.val < other.val ### HERE
        if not lists:
            return None
        curr = head = ListNode()
        h=[]
        for l in lists:
            if l:
                heapq.heappush(h,l)
        while h:
            curr.next = heapq.heappop(h)
            curr=curr.next
            if curr.next:
                heapq.heappush(h,curr.next)
            
        return head.next
    
#variant: input list of integer arrays
class Solution2:
    def mergeKLists(self, lists):
        if not lists:
            return []
        result = []
        h =[]
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(h,(l[0],i,1))
        while h:
            val,listi,i = heapq.heappop(h)
            result.append(val)  #might need to skip dups
            if i<len(lists[listi]):
                heapq.heappush(h,(lists[listi][i],listi,i+1))
        return result
    
#variant: implement iterator
class Solution3:
    def __init__(self,lists):
        self.lists = lists
        self.heap = []
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(self.heap,(l[0],i,1))
    def hasNext(self):
        return len(self.heap) > 0
    def next(self):
        if not self.hasNext():
            raise Exception()
        val,listi,i = heapq.heappop(self.heap)
        if i<len(self.lists[listi]):
            heapq.heappush(self.heap,(self.lists[listi][i],listi,i+1))
        return val

s=Solution2()
assert s.mergeKLists([[1,4,5],[1,3,4],[2,6]]) == [1,1,2,3,4,4,5,6]

s=Solution3([[1,4,5],[1,3,4],[2,6]])
assert s.hasNext()==True
for i in [1,1,2,3,4,4,5,6]:
    assert s.hasNext() == True
    assert s.next() == i
assert s.hasNext() == False
threw = False
try:
    s.next()
except:
    threw = True
assert threw