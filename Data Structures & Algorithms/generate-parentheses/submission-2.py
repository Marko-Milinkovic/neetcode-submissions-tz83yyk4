class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)]  # (string, opened, closed)
        
        while stack:
            current, opened, closed = stack.pop()
            
            if opened == closed == n:
                result.append(current)
                continue
            
            if opened < n:
                stack.append((current + "(", opened + 1, closed))
            
            if closed < opened:
                stack.append((current + ")", opened, closed + 1))
        
        return result
