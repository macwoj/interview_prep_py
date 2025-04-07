
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vect = []
        for i,v in enumerate(nums):
            if v>0:
                self.vect.append((i,v))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = j = 0
        result =0
        while i < len(self.vect) and j < len(vec.vect):
            if self.vect[i][0] == vec.vect[j][0]:
                result += self.vect[i][1]*vec.vect[j][1]
                i += 1
                j += 1
            elif self.vect[i][0] < vec.vect[j][0]:
                i += 1
            else:
                j += 1
        return result

# variant: what if the size differ drastically
# O(L1logL2) L1 length of shorter vector, L2 length of longer

class SparseVector2:
    def __init__(self, nums: List[int]):
        self.vect = []
        for i,v in enumerate(nums):
            if v>0:
                self.vect.append((i,v))
    
    def binSearch(self,vect,target):
        lo = 0
        hi = len(vect)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if vect[mid][0] == target:
                return vect[mid][1]
            if vect[mid][0] < target:
                lo=mid+1
            else:
                hi=mid-1
        return 0


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector2') -> int:
        i = j = 0
        result =0
        if len(vec.vect) < len(self.vect):
            for v in vec.vect:
                result += v[1]*self.binSearch(self.vect,v[0])
        else:
            for v in self.vect:
                result += v[1]*self.binSearch(vec.vect,v[0])
        
        return result
    

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]

a = SparseVector(nums1)
b = SparseVector2(nums1)
print(f'{a.dotProduct(SparseVector(nums2))} {b.dotProduct(SparseVector2(nums2))}')

nums1 = [1,0,0,2,3]
nums2 = [5]

a = SparseVector(nums1)
b = SparseVector2(nums1)
print(f'{a.dotProduct(SparseVector(nums2))} {b.dotProduct(SparseVector2(nums2))}')