'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = s.replace(" ","")
        s = ''.join([i for i in s if i.isalnum()])
        for i in range(len(s)):
            if s[i].lower() != s[(len(s)-1-i)].lower():
                return False
        return True
