
from typing import List

# Onlogn
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result = []
    for i in intervals:
        if not result or result[-1][1] < i[0]:
            result.append(i)
        else:
            result[-1][1] = max(result[-1][1],i[1])
        
    return result

#variant: given 2 arrays, intervals in A have no overlap, already sorted
# Oa+b space O1 ( result is aux space)
def merge2(a,b):
    i=j=0
    result =[]
    while i<len(a) or j<len(b):
        curr = None
        if i<len(a) and j<len(b):
            if a[i][0] <= b[j][0]:
                curr = a[i]
                i+=1
            else:
                curr = b[j]
                j+=1
        elif i<len(a):
            curr = a[i]
            i+=1
        elif j<len(b):
            curr=b[j]
            j+=1
        if curr:
            if not result or result[-1][1] < curr[0]:
                result.append(curr)
            else:
                result[-1][1] = max(result[-1][1],curr[1])
        
    return result


print(merge2([[3,11], [14,15], [18,22], [23,24], [25,26]],[[2,8], [13,20]])) # [[2, 11], [13, 22], [23, 24], [25, 26]]
print(merge2([],[[0,4],[10,13]])) # 0,4  10,13