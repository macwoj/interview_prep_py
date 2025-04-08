
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# On space O1
def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    pp = p
    qq = q
    while qq != pp:
        qq = qq.parent if qq.parent else q
        pp = pp.parent if pp.parent else p
    return qq

# variant: type changes to char/str
# no changes in implementation

#variant: also given a list of all the nodes, unordered
# On space On

class Node2:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(self, p: 'Node2', q: 'Node2', nodes: List[Node2]) -> 'Node2':
    parent = {}
    for n in nodes:
        if n.left:
            parent[n.left] = n
        if n.right:
            parent[n.right] = n
    pp = p
    qq = q
    while qq!=pp:
        qq = parent[qq] if qq in parent else q
        pp = parent[pp] if pp in parent else p
    return qq