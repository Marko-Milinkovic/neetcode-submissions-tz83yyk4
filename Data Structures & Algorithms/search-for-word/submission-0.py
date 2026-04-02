class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(ROWS):
            for j in range(COLS):
                if (board[i][j] == word[0]):
                    
                    stack = [(i, j, 0, {(i, j)})]

                    while stack:
                        r, c, idx, visited = stack.pop()
                        if idx == len(word) - 1:
                            return True
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == word[idx + 1] and (nr, nc) not in visited:
                                new_visited = visited | {(nr, nc)}
                                stack.append((nr, nc, idx + 1, new_visited))

        return False


