

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# On space: On
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        nodes = {None:None}
        node = head
        while node:
            nodes[node] = Node(node.val)
            node = node.next
        node=head
        while node:
            nodes[node].next = nodes[node.next]
            nodes[node].random = nodes[node.random]
            node=node.next
        return nodes[head]
    
# variant: deep copy binary tree with rand ptr, lc 1485
# 2*On space:On
class Node2:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution2:
    def copyRandomBinaryTree(self, root: 'Optional[Node2]') -> 'Optional[NodeCopy]':
        nodes = {None:None}
        def dfs(node):
            nonlocal nodes
            if not node:
                return None
            if node not in nodes:
                nodes[node] = NodeCopy(node.val)
            if node.random and node.random not in nodes:
                nodes[node.random]=NodeCopy(node.random.val)
            nodes[node].random = nodes[node.random]
            nodes[node].left = dfs(node.left)
            nodes[node].right = dfs(node.right)
            return nodes[node]
        dfs(root)
        return nodes[root]