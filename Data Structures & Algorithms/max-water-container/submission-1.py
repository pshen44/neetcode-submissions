class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #since len(height) always >= 2 set pointers
        l, r = 0, 1
        res = 0

        while r < len(heights):
            res = max(res, ( (r - l) * min(heights[r], heights[l])) )
            if heights[r] > heights[l]:
                l = r
            else:
                r += 1
        return res