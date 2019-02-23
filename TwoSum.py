'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        dict = {value: index for (index,value) in enumerate(nums)}
        
        for(i,v) in enumerate(nums):
            targetNum = target - v
            
            if targetNum in dict and dict[targetNum] != i:
                return[i,dict[targetNum]]
