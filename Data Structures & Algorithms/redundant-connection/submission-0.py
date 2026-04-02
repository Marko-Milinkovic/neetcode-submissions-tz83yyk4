class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # since graph has n nodes and n edges
        parent = list(range(n + 1))   # 1-indexed
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False  # already connected -> adding this edge forms a cycle
            # union by rank
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        redundant = None
        for u, v in edges:
            if not union(u, v):
                redundant = [u, v]   # record; don't break to ensure we keep the last one

        return redundant
