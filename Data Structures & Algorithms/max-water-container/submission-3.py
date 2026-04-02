class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # area = (left - right) * min(heights[left], heights[right])

        area = 0

        p = 0
        q = len(heights) - 1

        while p < q:

            cur = (q - p) * min(heights[p], heights[q])

            if heights[p] <= heights[q]:
                p += 1
            else:
                q -= 1

            if cur > area:
                area = cur
        
        return area
