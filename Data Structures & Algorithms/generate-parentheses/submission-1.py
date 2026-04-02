class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = [("", 0, 0)]
        result = []

        while stack:
            path, numOfLeft, numOfRight = stack.pop()

            if numOfLeft == numOfRight == n:
                result.append(path)

            if numOfLeft < n:
                stack.append((path + '(', numOfLeft + 1, numOfRight))
            
            if numOfRight < numOfLeft:
                stack.append((path + ')', numOfLeft, numOfRight + 1))
        
        return result
