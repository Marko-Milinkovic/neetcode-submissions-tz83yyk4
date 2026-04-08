class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []

        for i,v in enumerate(temperatures):

            while stack and stack[-1][1] < v:
                
                stack_ind , stack_temp = stack.pop()
                result[stack_ind] = i - stack_ind

            stack.append((i,v))
        
        return result