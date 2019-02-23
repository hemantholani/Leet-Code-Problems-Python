'''

Given a string, find the length of the longest substring without repeating characters.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        sub = ''
        count = 0
        for ch in s:
            if ch not in sub:
                sub += ch
                if len(sub)>count:
                    count=len(sub)
            else:
                print(sub)
                print(sub.split(ch))
                sub = sub.split(ch)[-1] + ch
                print(sub)
        return(count)
                
        
