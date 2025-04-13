
from collections import deque
from typing import List

# On^2 space On

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        q = deque([(1,0,0)])
        dirs = [(1,1),(-1,-1),(-1,1),(1,-1),(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            d,r,c = q.popleft()
            if r == n-1 and c==n-1:
                return d
            for y,x in dirs:
                row = r+y
                col = c+x
                if row >=0 and row < n and col >= 0 and col < n and grid[row][col] == 0:
                    grid[row][col] = 1
                    q.append((d+1,row,col))
        return -1
    
#variant: return path
#On^3 (copy), 
class Solution2:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]):
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[-1][-1]:
            return []
        q = deque([([[0,0]],0,0)])
        dirs = [(1,1),(-1,-1),(-1,1),(1,-1),(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            path,r,c = q.popleft()
            if r == n-1 and c==n-1:
                return path
            for y,x in dirs:
                row = r+y
                col = c+x
                if row >=0 and row < n and col >= 0 and col < n and grid[row][col] == 0:
                    grid[row][col] = 1
                    q.append((path[:]+[[row,col]],row,col))
        return []
    
#variant: return path, dfs solution
class Solution3:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]):
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[-1][-1]:
            return []
        dirs = [(1,1),(-1,-1),(-1,1),(1,-1),(1,0),(0,1),(-1,0),(0,-1)]
        result=[]
        def dfs(r,c):
            nonlocal dirs,grid,result
            grid[r][c]=1
            result.append([r,c])
            if r == n-1 and c==n-1:
                return True
            for y,x in dirs:
                row = r+y
                col = c+x
                if row >=0 and row < n and col >= 0 and col < n and grid[row][col] == 0:
                    if dfs(row,col):
                        return True
            result.pop()
        dfs(0,0)
        return result
    
s = Solution2()
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
s = Solution3()
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))