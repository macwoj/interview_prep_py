
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    result = 0
    def dfs(node):
        nonlocal result
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        result = max(result,left+right)
        return max(left,right) + 1
    dfs(root)
    return result

#variant: n-ary tree, 1522 leetcode


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


def diameter(self, root: 'Node') -> int:
    result = 0
    """
    :type root: 'Node'
    :rtype: int
    """
    def dfs(root):
        nonlocal result
        if not root:
            return 0
        max_h0 = max_h1 = 0
        for c in root.children:
            res = dfs(c)
            if res > max_h0:
                max_h1 = max_h0
                max_h0 = res
            elif res > max_h1:
                max_h1 = res
        result = max(result,max_h0+max_h1)
        return max(max_h0,max_h1)+1
    dfs(root)
    return result