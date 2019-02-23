'''
Given a 32-bit signed integer, reverse digits of an integer.
'''
class Solution:
    def reverse(self, x: 'int') -> 'int':
        s = (str(x))
        if s[len(s)-1] is 0:
            s[len(s)-1] = ""
        if "-" in s:
            sp = s.split("-")
            s = sp[1][::-1]
            i = int("-" + s)
            
        else:
            s = s[::-1]
            i = int(s)
        if abs(i) < ((2**31)-1):
            return(i)
        else:
            return(0)
