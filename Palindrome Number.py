'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        s = s[::-1]
        print(s)
        if x<0:
            return(False)
        else:
            p = int(s)
            if p == x:
                print(p)
                return(True)
            else:
                return(False)
