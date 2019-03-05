'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red,white,blue = 0,0,len(nums)-1
        while(white<=blue):
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white = white + 1
                red = red + 1
            elif nums[white] == 1:
                white = white + 1
            else:
                nums[white],nums[blue] = nums[blue],nums[white]
                blue = blue - 1
            print(nums)
