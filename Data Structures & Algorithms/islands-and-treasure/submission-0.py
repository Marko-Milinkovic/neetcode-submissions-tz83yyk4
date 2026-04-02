class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        INF = 2147483647

        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            r, c = queue.popleft()

            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue
                
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))

