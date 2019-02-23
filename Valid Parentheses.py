'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        if len(s) is 1:
            return False
        for ch in s:
            if ch in mapping:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = 'h'
                if mapping[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return not stack
            
