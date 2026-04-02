class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []


        for i,v in enumerate(temperatures):

            while stack and v > stack[-1][1]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()

            stack.append((i,v))
        
        return result