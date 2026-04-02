class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        graph = {i : [] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque([0])

        while queue:
            cur = queue.popleft()
            
            if cur in visited:
                continue
            visited.add(cur)

            for nei in graph[cur]:
                if nei not in visited:
                    queue.append(nei)
        
        return len(visited) == n
