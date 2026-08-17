class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        length = len(heights)
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index

            stack.append((start, h))
        
        for i, h in stack:
            area = max(area, h * (length - i))
        
        return area