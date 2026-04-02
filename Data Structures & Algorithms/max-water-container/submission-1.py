class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area  = min(heights[p], heights[q]) * (p - q)
        p = 0
        q = len(heights) - 1
        
        result = 0
        while p < q:
            area = min(heights[p], heights[q]) * (q - p)
            if area > result:
                result = area
            
            if (heights[p] < heights[q]):
                p += 1
            else:
                q -= 1

        return result