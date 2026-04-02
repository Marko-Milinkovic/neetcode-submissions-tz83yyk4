class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []


        for i in range(len(temperatures)):
            
            if i == len(temperatures) - 1:
                result[i] = 0
                continue

            if temperatures[i] < temperatures[i + 1]:
                result[i] = 1
                continue
            

            j = i + 1
            # Add the 'j < len(temperatures)' check first
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1

            # If j reached the end without finding a warmer day, result is 0
            if j < len(temperatures):
                result[i] = (j - i)
            else:
                result[i] = 0
        
        return result


