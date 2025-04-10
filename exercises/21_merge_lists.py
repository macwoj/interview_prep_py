
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(-101)
        head = curr
        l1 = list1
        l2=list2
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.ext=l2
                l2=l2.next
            curr=curr.next
        curr.next = l1 if l1 else l2
        return head.next
    
#variant: merge 3 lists, only use aux space, input is list
#Oa+b+c space:O1
def merge3(listA,listB,listC):
    result = []
    a,b,c=0,0,0
    while a<len(listA) or b<len(listB) or c<len(listC):
        val_a=listA[a] if a<len(listA) else float('inf')
        val_b=listB[b] if b<len(listB) else float('inf')
        val_c=listC[c] if c<len(listC) else float('inf')
        val = min(val_a,val_b,val_c)
        result.append(val)
        if val == val_a:
            a+=1
        elif val == val_b:
            b+=1
        else:
            c+=1

    return result

#variant: 3 lists, no dups in result
#Oa+b+c space:O1
def merge3_2(listA,listB,listC):
    result = []
    a,b,c=0,0,0
    while a<len(listA) or b<len(listB) or c<len(listC):
        val_a=listA[a] if a<len(listA) else float('inf')
        val_b=listB[b] if b<len(listB) else float('inf')
        val_c=listC[c] if c<len(listC) else float('inf')
        val = min(val_a,val_b,val_c)
        if not result or result[-1]!=val:
            result.append(val)
        if val == val_a:
            a+=1
        elif val == val_b:
            b+=1
        else:
            c+=1

    return result


a = [1, 1, 1, 3, 4, 5]
b = [3, 3, 4, 5, 6]
c = [1, 1, 3, 3, 8, 8, 8, 10]
expected = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 8, 8, 10]
assert expected == merge3(a, b, c)

a = []
b = [3, 3, 4, 5, 6]
c = [1, 1, 3, 3, 8, 8, 8, 10]
expected = [1, 1, 3, 3, 3, 3, 4, 5, 6, 8, 8, 8, 10]
assert expected == merge3(a, b, c)

a = []
b = []
c = []
expected = []
assert expected == merge3(a, b, c)

a = [1]
b = [2]
c = [3, 4, 5, 6, 7]
expected = [1, 2, 3, 4, 5, 6, 7]
assert expected == merge3(a, b, c)

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]
expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
assert expected == merge3(a, b, c)

a = [2, 2]
b = [2]
c = [0]
expected = [0, 2, 2, 2]
assert expected == merge3(a, b, c)

#-----------------
a = [1, 1, 1, 3, 4, 5]
b = [3, 3, 4, 5, 6]
c = [1, 1, 3, 3, 8, 8, 8, 10]
expected = [1, 3, 4, 5, 6, 8, 10]
assert expected == merge3_2(a, b, c)

a = []
b = [3, 3, 4, 5, 6]
c = [1, 1, 3, 3, 8, 8, 8, 10]
expected = [1, 3, 4, 5, 6, 8, 10]
assert expected == merge3_2(a, b, c)

a = []
b = []
c = []
expected = []
assert expected == merge3_2(a, b, c)

a = [1]
b = [2]
c = [3, 4, 5, 6, 7]
expected = [1, 2, 3, 4, 5, 6, 7]
assert expected == merge3_2(a, b, c)

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]
expected = [1, 2, 3]
assert expected == merge3_2(a, b, c)

a = [2, 2]
b = [2]
c = [0]
expected = [0, 2]
assert expected == merge3_2(a, b, c)