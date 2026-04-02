class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    
                    queue = deque([(i,j)])
                    visited.add((i,j))
                    area = 1

                    while queue:
                        r, c  = queue.popleft()
                        
                        for direction in directions:
                            nr, nc = r + direction[0], c + direction[1]
                            if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                                continue
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                                area += 1

                    maxArea = max(maxArea, area)

        return maxArea