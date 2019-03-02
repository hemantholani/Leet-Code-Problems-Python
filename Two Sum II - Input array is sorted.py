'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sumleft = {}
        for i,v in enumerate(numbers):
            if v not in sumleft.values():
                sumleft[v] = target-v
            else:
                j = numbers.index(target-v)
                return [j+1,i+1]
