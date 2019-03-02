'''
Given an input string, reverse the string word by word.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        print(words)
        output = ""
        for i in reversed(words):
            if len(i) != 0:
                print(i)
                output = output + i + " "
        return(output[:-1])
