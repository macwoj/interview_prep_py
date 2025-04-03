
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(self, root: Optional[TreeNode], target: float) -> int:
    if not root:
        return -1
    best = None
    result = -1
    while root:
        dist = abs(root.val - target)
        if best is None or dist < best or (dist==best and root.val<result):
            best = dist
            result=root.val
        if root.val < target:
            root=root.right
        else:
            root=root.left

    return result

#variant: target is int