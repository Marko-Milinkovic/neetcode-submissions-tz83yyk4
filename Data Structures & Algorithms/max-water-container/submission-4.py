class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        # area  = (r - l) * min(heights[l], heights[r])

        l = 0
        r = len(heights) - 1

        result = 0
        for i in range(len(heights)):

            area = (r - l) * min(heights[l], heights[r])
            if area > result:
                result = area
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return result

