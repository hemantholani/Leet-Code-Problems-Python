'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''
class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        out = []
        found = False
        for i,v in enumerate(nums):
            if not found and v == target:
                out.append(i)
                found = True
            elif found and v != target:
                out.append(i-1)
                return out
            elif found and i == len(nums)-1:
                out.append(i)
                return out
        if found:
            out.append(out[0])
            return out
        else:
            return [-1,-1]
