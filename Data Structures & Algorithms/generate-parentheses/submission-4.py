class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        stack = [("" , 0 , 0)]


        while stack:

            current , open_cnt , closed_cnt = stack.pop()

            if open_cnt == closed_cnt == n:
                result.append(current)
                continue

            if open_cnt < n:
                stack.append((current + "(" , open_cnt + 1, closed_cnt))
            
            if closed_cnt < open_cnt:
                stack.append((current + ")", open_cnt, closed_cnt + 1))

        return result
                