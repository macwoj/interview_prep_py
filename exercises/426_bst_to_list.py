
from typing import Optional

#On space: On
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        head = None
        last = None
        # O(n)
        def dfs(node):
            nonlocal head,last
            if not node:
                return
            dfs(node.left)
            if not head:
                head = node
            if not last:
                last = node
            else:
                last.right = node
                node.left = last
                last = node
            dfs(node.right)
        dfs(root)
        head.left = last
        last.right = head
        return head

#variant: binary tree, inorder traversal
# same impl