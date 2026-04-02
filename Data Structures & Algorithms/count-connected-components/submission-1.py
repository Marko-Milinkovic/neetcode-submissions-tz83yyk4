class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i : [] for i in range(n)}
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        res = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                res += 1
        
        return res
