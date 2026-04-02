class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(sr, sc):
            stack = [(sr, sc, 0, {(sr, sc)})]  # (row, col, index in word, visited set)
            
            while stack:
                r, c, idx, visited = stack.pop()
                
                # If we matched all characters → success
                if idx == len(word) - 1:
                    return True
                
                # Explore 4 directions
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    
                    # Check boundaries + not visited + correct next letter
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        (nr, nc) not in visited and 
                        board[nr][nc] == word[idx + 1]):
                        
                        new_visited = set(visited)
                        new_visited.add((nr, nc))
                        stack.append((nr, nc, idx + 1, new_visited))
            
            return False
        
        # Try DFS for each matching first letter
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c):
                        return True
        
        return False
