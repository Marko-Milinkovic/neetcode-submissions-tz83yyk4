class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        hottest = 0

        for i in range(n - 1, -1 , -1):

            current = temperatures[i]
            if current >= hottest:
                hottest = current
                continue

            if temperatures[i] < temperatures[i + 1]:
                res[i] = 1
                continue
            
            j = i + 1
            while j < n and temperatures[j] <= current:
                
                j = j + res[j]

            res[i] = j - i

        
        return res
                

