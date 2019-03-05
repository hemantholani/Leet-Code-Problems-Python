'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        words = s.split(' ')
        print(words)
        while "" in words:
            words.remove("")
        if len(words) != 0:
            return len(words[-1])
        else:
            return 0
