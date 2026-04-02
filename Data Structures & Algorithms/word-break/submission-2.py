from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)   # O(1) membership checks
        n = len(s)
        
        queue = deque([0])         # start index
        visited = set()            # indices we’ve already processed
        
        while queue:
            start = queue.popleft()
            if start == n:         # reached end of string
                return True
            
            if start in visited:
                continue
            visited.add(start)
            
            for word in word_set:
                end = start + len(word)
                if end <= n and s[start:end] == word:
                    queue.append(end)
        
        return False
