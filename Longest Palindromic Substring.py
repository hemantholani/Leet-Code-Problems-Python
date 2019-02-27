'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s
        def expand(s,left,right):
            l,r = left,right
            while(l>=0 and r <=len(s)-1 and s[l] == s[r]):
                l = l - 1
                r = r + 1
            return s[l+1:r]
        left = 0
        right = 0
        ans = ""
        for i in range(len(s)):
            s1 = expand(s,i,i)
            if len(s1)>len(ans):
                ans = s1
            s2 = expand(s,i,i+1)
            if len(s2)>len(ans):
                ans = s2
        return ans
