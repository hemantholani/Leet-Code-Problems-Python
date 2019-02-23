'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''
class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if target in nums:
            return nums.index(target)
        else:
            for i,v in enumerate(nums):
                if v>target:
                    return i
            return len(nums)
