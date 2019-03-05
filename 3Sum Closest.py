'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
            
        nums.sort()
        output = sum(nums[:3])
        for index,value in enumerate(nums):
            left = index + 1
            right = len(nums)-1
            while left<right:
                total = value + nums[left] + nums[right]
                if abs(target-total) < abs(target-output):
                    output = total
                if total < target:
                    left = left + 1
                elif total > target:
                    right = right - 1
                else:
                    return output
        return output
