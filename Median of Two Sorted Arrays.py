'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        full_list = nums1+nums2
        full_list.sort()
        print(full_list)
        if len(full_list)%2!=0:
            median = full_list[int((len(full_list))/2)]
        else:
            median = (full_list[int((len(full_list))/2)] + full_list[int((len(full_list)-1)/2)])/2
        return(median)
        
