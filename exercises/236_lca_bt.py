
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root,p,q):
        if not root:
            return None
        left = self.dfs(root.left,p,q)
        right = self.dfs(root.right,p,q)
        if left and right:
            return root
        elif root == p or root == q:
            return root
        return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q)
    
class Node:
    def __init__(self, x):
        self.val = x
        self.children=[]
# variant: n-ary tree
class Solution2:
    def dfs(self,root,p,q):
        if not root:
            return None
        nodes=[]
        for c in root.children:
            tmp = self.dfs(c,p,q)
            if tmp:
                nodes.append(tmp)
        if len(nodes)==2:
            return root
        elif root == p or root == q:
            return root
        return nodes[0] if nodes else None

    def lowestCommonAncestor(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        return self.dfs(root,p,q)

# Tree structure:
#       1
#    /  |  \
#   3   2   4
#  / \
# 5   6
root1 = Node(1)
node3 = Node(3)
node2 = Node(2)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

root1.children = [node3, node2, node4]
node3.children = [node5, node6]
solution = Solution2()
assert solution.lowestCommonAncestor(root1, node5, node2) == root1
assert solution.lowestCommonAncestor(root1, node5, node6) == node3

# Test Case 2: More complex tree
# Tree structure:
#        10
#     /  |  \  \
#    5   1   7  8
#   / \  |      |
#  2  4  3      9
#    /
#   6
root2 = Node(10)
node5_2 = Node(5)
node1 = Node(1)
node7 = Node(7)
node8 = Node(8)
node2_2 = Node(2)
node4_2 = Node(4)
node3_2 = Node(3)
node9 = Node(9)
node6_2 = Node(6)

root2.children = [node5_2, node1, node7, node8]
node5_2.children = [node2_2, node4_2]
node1.children = [node3_2]
node8.children = [node9]
node4_2.children = [node6_2]
assert solution.lowestCommonAncestor(root2, node6_2, node3_2) == root2
assert solution.lowestCommonAncestor(root2, node6_2, node2_2) == node5_2

# Tree structure:
#       1
#    /  |  \
#   2   3   4
#  / \     / | \
# 5   6   7  8  9
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
root.children = [node2, node3, node4]
node2.children = [node5, node6]
node4.children = [node7, node8, node9]
solution = Solution2()
# Root as the LCA
assert solution.lowestCommonAncestor(root, node5, node7) == root
assert solution.lowestCommonAncestor(root, node5, node8) == root
assert solution.lowestCommonAncestor(root, node5, node9) == root
assert solution.lowestCommonAncestor(root, node6, node7) == root
assert solution.lowestCommonAncestor(root, node6, node8) == root
assert solution.lowestCommonAncestor(root, node6, node9) == root

assert solution.lowestCommonAncestor(root, node2, node9) == root

assert solution.lowestCommonAncestor(root, node2, node4) == root
assert solution.lowestCommonAncestor(root, node2, node3) == root

# Node 4 as the LCA
assert solution.lowestCommonAncestor(root, node7, node8) == node4
assert solution.lowestCommonAncestor(root, node7, node9) == node4

# Node 2 as the LCA
assert solution.lowestCommonAncestor(root, node5, node6) == node2

# Same tree structure for the second test case:
#       1
#    /  |  \
#   2   3   4
#  / \     / | \
# 5   6   7  8  9
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

root.children = [node2, node3, node4]
node2.children = [node5, node6]
node4.children = [node7, node8, node9]

solution = Solution2()
# Root as the LCA
assert solution.lowestCommonAncestor(root, root, node2) == root
assert solution.lowestCommonAncestor(root, root, node3) == root
assert solution.lowestCommonAncestor(root, root, node4) == root
assert solution.lowestCommonAncestor(root, root, node5) == root
assert solution.lowestCommonAncestor(root, root, node6) == root
assert solution.lowestCommonAncestor(root, root, node7) == root
assert solution.lowestCommonAncestor(root, root, node8) == root
assert solution.lowestCommonAncestor(root, root, node9) == root

# Node 4 as the LCA
assert solution.lowestCommonAncestor(root, node4, node8) == node4
assert solution.lowestCommonAncestor(root, node4, node9) == node4

# Node 2 as the LCA
assert solution.lowestCommonAncestor(root, node2, node6) == node2