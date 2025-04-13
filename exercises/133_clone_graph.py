
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def dfs(node):
            nonlocal visited
            if node in visited:
                return visited[node]
            visited[node]=Node(node.val)
            for n in node.neighbors:
                visited[node].neighbors.append(dfs(n))
            return visited[node]
        return dfs(node)
    
#variant: disconnected undirected graph
# O(n+e) n-nodes e edges, space On n-nodes

class Graph:
    def __init__(self):
        self.roots=[]

class Solution2:
    def cloneGraph(self, graph):
        result = Graph()
        def dfs(node,visited):
            if node in visited:
                return visited[node]
            visited[node]=Node(node.val)
            for n in node.neighbors:
                visited[node].neighbors.append(dfs(n,visited))
            return visited[node]
        for root in graph.roots:
            if not root:
                continue
            visited = {}
            result.roots.append(dfs(root,visited))
        return result