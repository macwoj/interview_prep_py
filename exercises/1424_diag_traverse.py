





from collections import deque
from typing import List

#On storage Osqrt(n)
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([(0,0)])
        result = []
        while q:
            r,c = q.popleft()
            result.append(nums[r][c])
            if c==0 and r+1 < len(nums):
                q.append((r+1,c))
            if c + 1 < len(nums[r]):
                q.append((r,c+1))
        return result
    
#variant: anti diagonal order, return nested lists
#On storage Osqrt(n)
class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([(0,0)])
        result = []
        while q:
            n = range(len(q))
            tmp = []
            for i in n:
                r,c = q.popleft()
                tmp.append(nums[r][c])
                if r==0 and c+1<len(nums[0]):
                    q.append((r,c+1))
                if r+1<len(nums):
                    q.append((r+1,c))
            result.append(tmp)
        return result

#variant: matrix m x n, antidignoal, print result
#On storage: O1
class Solution3:
    def printDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = len(nums[0])
        def print_diag(r,c):
            nonlocal nums,n
            while r<m and c>=0:
                print(nums[r][c],end=' ')
                r+=1
                c-=1
            print()
        for c in range(m):
            print_diag(0,c)
        for r in range(1,n):
            print_diag(r,n-1)
s = Solution2()
assert s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1], [2, 4], [3, 5, 7], [6, 8], [9]]

s=Solution3()
s.printDiagonalOrder([[9,8,6],[7,5,3],[4,2,1]])