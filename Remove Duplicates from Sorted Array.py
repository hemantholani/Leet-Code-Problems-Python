'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        prev = 0
        if len(nums) is 0:
            return(0)
        for i in range(1,len(nums)):
            if nums[i] != nums[prev]:
                prev = prev + 1
                nums[prev] = nums[i]
        return(prev + 1)
            
