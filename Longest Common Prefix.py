'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs: 
            return("")
        minStr = min(strs, key=len)
        minLen = len(minStr)
        matching = False
        while minLen>0:
            matching = True
            for s in strs:
                if s[:minLen] == minStr[:minLen]:
                    matching = matching and True
                else:
                    matching = False
            if matching:
                return(minStr[:minLen])
            minLen = minLen-1
            
        return("")
