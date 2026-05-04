# Задача:
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=problem-list-v2&envId=dsa-linear-shoal-monotonic-stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0
    
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
        
            stack.append(i)
    
        return max_area
