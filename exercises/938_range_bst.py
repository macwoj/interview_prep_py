

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#On if balanced Ologn, space On

def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    sta = [root]
    result = 0
    while sta:
        node = sta.pop()
        if node.val >= low and node.val <= high:
            result+=node.val
        if node.left and node.val > low:
            sta.append(node.left)
        if node.right and node.val < high:
            sta.append(node.right)
    return result


#variant: return the avg

def rangeSumBST2(root: Optional[TreeNode], low: int, high: int) -> int:
    sta = [root]
    result = 0
    count = 0
    while sta:
        node = sta.pop()
        if node.val >= low and node.val <= high:
            result+=node.val
            count+=1
        if node.left and node.val > low:
            sta.append(node.left)
        if node.right and node.val < high:
            sta.append(node.right)
    return float(result)/float(count)

#variant: function called many times
# up front On, each call Ologn space On

class Solution:
    def __init__(self,root):
        self.vals=[]
        self.prefix=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.vals.append(node.vals)
            if not self.prefix:
                self.prefix.append(node.vals)
            else:
                self.prefix.append(node.vals+self.prefix[-1])
            inorder(node.right)
        inorder(root)
    def leftBound(self,lower):
        lo=0
        hi=len(self.vals)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if lower <= self.vals[mid]:
                hi=mid-1
            else:
                lo=mid+1
        return lo
    def rightBound(self,upper):
        hi=len(self.vals)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if self.vals[mid] <= upper:
                lo=mid+1
            else:
                hi=mid-1
        return hi

    def range(self,lower,upper):
        left=self.leftBound(lower)
        right=self.rightBound(upper)
        if left ==0:
            return self.prefix[right]
        else:
            self.prefix[right]-self.prefix[left-1]
