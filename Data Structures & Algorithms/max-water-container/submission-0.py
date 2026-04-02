class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        result = 0

        for i in range(len(heights)):
            P = (right - left) * min(heights[left], heights[right])

            if (result < P):
                result = P
            
            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        
        return result