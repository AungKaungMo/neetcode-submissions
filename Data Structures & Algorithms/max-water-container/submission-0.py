class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        # for key, val in enumerate(heights):
        while l < r:
            width = r - l
            min_height = min(heights[l], heights[r])
            area = width * min_height

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -=1
            else:
                l += 1
                r -= 1

            if area > res:
                res = area
        
        return res
