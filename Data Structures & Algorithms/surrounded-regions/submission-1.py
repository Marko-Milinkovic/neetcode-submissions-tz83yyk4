class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board or not board[0]:
            return None
        
        ROWS, COLS = len(board), len(board[0])

        def bfs(r, c):
            
            queue = deque([(r, c)])
            board[r][c] = "S"

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while queue:
                row, col = queue.popleft()
                for direction in directions:
                    nrow, ncol = row + direction[0], col + direction[1]
                    if (0 <= nrow < ROWS) and (0 <= ncol < COLS) and board[nrow][ncol] == "O":
                        board[nrow][ncol] = "S"
                        queue.append((nrow, ncol))
            
        
        for r in range(ROWS):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][COLS - 1] == "O":
                bfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                bfs(0, c)
            if board[ROWS - 1][c] == "O":
                bfs(ROWS - 1, c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] ="O"



