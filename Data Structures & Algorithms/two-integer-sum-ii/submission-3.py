class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if numbers is None:
            return []

        p = 0
        q = len(numbers) - 1

        while p <= q:

            if numbers[p] + numbers[q] == target:
                return [p + 1, q + 1]
            
            if numbers[p] + numbers[q] < target:
                p += 1
            
            if numbers[p] + numbers[q] > target:
                q -= 1
        
        return []
