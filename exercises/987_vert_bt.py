

from collections import defaultdict, deque
from typing import List, Optional

#O(n/c log(n/c)) c-columns 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        nodes = defaultdict(list)
        q.append((root,(0,0)))
        min_col = 0
        max_col = 0
        while len(q) > 0:
            node,pos = q.popleft()
            min_col = min(min_col,pos[1])
            max_col = max(max_col,pos[1])
            nodes[pos[1]].append((pos[0],node.val))
            if node.left:
                q.append((node.left,(pos[0]+1,pos[1]-1)))
            if node.right:
                q.append((node.right,(pos[0]+1,pos[1]+1)))
        result=[]
        for k in range(min_col,max_col+1):
            nodes[k].sort()
            result.append([n[1] for n in nodes[k]])
        return result
    
#variant: print result
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        nodes = defaultdict(list)
        q.append((root,(0,0)))
        min_col = 0
        max_col = 0
        while len(q) > 0:
            node,pos = q.popleft()
            min_col = min(min_col,pos[1])
            max_col = max(max_col,pos[1])
            nodes[pos[1]].append((pos[0],node.val))
            if node.left:
                q.append((node.left,(pos[0]+1,pos[1]-1)))
            if node.right:
                q.append((node.right,(pos[0]+1,pos[1]+1)))

        for k in range(min_col,max_col+1):
            nodes[k].sort()
            for n in nodes[k]:
                print(n,end=' ')
            print()

#variant: 1d vertical order, single list as return

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        nodes = defaultdict(list)
        q.append((root,(0,0)))
        min_col = 0
        max_col = 0
        while len(q) > 0:
            node,pos = q.popleft()
            min_col = min(min_col,pos[1])
            max_col = max(max_col,pos[1])
            nodes[pos[1]].append((pos[0],node.val))
            if node.left:
                q.append((node.left,(pos[0]+1,pos[1]-1)))
            if node.right:
                q.append((node.right,(pos[0]+1,pos[1]+1)))
        result=[]
        for k in range(min_col,max_col+1):
            nodes[k].sort()
            for n in nodes[k]:
                result.append(n[1])
        return result