'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        return int(2*sum(list(set(nums)))-sum(nums))
