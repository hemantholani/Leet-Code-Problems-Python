'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
            
        nums.sort()
        output = []
        for index,value in enumerate(nums):
            left = index + 1
            right = len(nums)-1
            while left<right:
                if value + nums[left] + nums[right] == 0 :
                    if sorted([value, nums[left], nums[right]]) not in output:
                        output.append(sorted([value, nums[left], nums[right]]))
                    right = right - 1
                elif value + nums[left] + nums[right] < 0:
                    left = left + 1
                else:
                    right = right - 1
        return output
