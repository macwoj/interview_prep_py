# On space: On

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        n = len(q)
        for i in range(n):
            node=q.popleft()
            if i==n-1:
                result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result

#variant: left and right side view, left side bottom to top then right side top to bottom, root only once
# might get asked to push both sides in one array
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q =deque([root])
    left_view = []
    right_view = []
    while q:
        n=len(q)
        for i in range(n):
            node=q.popleft()
            if i==0:
                left_view.append(node.val)
            if i==n-1:
                right_view.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    result = list(reversed(left_view))
    result.extend(right_view)
    return result

#variant print
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    q =deque([root])
    left_view = []
    right_view = []
    while q:
        n=len(q)
        for i in range(n):
            node=q.popleft()
            if i==0:
                left_view.append(node.val)
            if i==n-1:
                right_view.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    for n in reversed(left_view):
        print(n,end=' ')
    for i in right_view[1:]:
        print(i,end=' ')

