from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        neighbours = [[1,0], [-1, 0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        islands = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    # perform BFS
                    queue = deque([(i, j)])
                    islands += 1
                    visited.add((i, j))

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in neighbours:
                            nr, nc = r + dr, c + dc
                            if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                                continue
                            if (nr, nc) not in visited:
                                queue.append((nr, nc))
                                visited.add((nr, nc))

        return islands
