from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# On storage: Oh h=height
class Solution:
    def dfs(self,root, num):
        if not root:
            return 0
        curr = num*10 + root.val
        if not root.left and not root.right:
            return curr
        left = self.dfs(root.left,curr)
        right = self.dfs(root.right,curr)
        return left+right
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    
#variant: val can range from 0-999
# On storage: Oh h=height
class Solution2:
    def dfs(self,root, num):
        if not root:
            return 0
        mult = 1
        while root.val//mult > 0:
            mult*=10
        curr = num*mult + root.val
        if not root.left and not root.right:
            return curr
        left = self.dfs(root.left,curr)
        right = self.dfs(root.right,curr)
        return left+right
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    
#variant: value -9to9, each node to leaf is negative if the negative count is odd in the path
class Solution3:
    def dfs(self,root, num, neg_count):
        if not root:
            return 0
        curr = num*10 + abs(root.val)
        if root.val < 0:
            neg_count+=1
        if not root.left and not root.right:
            return curr if neg_count%2==0 else -curr
        left = self.dfs(root.left,curr,neg_count)
        right = self.dfs(root.right,curr,neg_count)
        return left+right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0,0)

s = Solution2()
print(s.sumNumbers(TreeNode(3,TreeNode(79,None,TreeNode(111)),TreeNode(2)))) # 379143

s = Solution3()
print(s.sumNumbers(TreeNode(-1,TreeNode(-2,TreeNode(-9),None),TreeNode(4,TreeNode(-5))))) # 16
print(s.sumNumbers(TreeNode(1,TreeNode(-2),TreeNode(3)))) # 1