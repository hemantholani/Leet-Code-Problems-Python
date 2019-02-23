'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        if len(height) == 2:
            return(min(height[0],height[1]))
        maxarea = 0
        left = 0
        right = len(height)-1
        while left<right:

            maxarea = max(maxarea,min(height[left],height[right])*(right-left))
           
            if height[left] <= height[right]:
                left = left+1
            else: 
                right = right-1
        return(maxarea)
