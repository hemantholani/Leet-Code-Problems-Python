'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
'''
class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        integer = ""
        negative = False
        minimum = -2**31
        maximum= (2**31)-1
        if not str.strip():
            return(0)
        index = next(i for i, j in enumerate(str) if j not in string.whitespace)
        
        
        if not str[index].isdigit() and str[index] is not "-" and str[index] is not "+":
            return(0)
        else:
            if str[index] is "-":
                negative = True
                index= index+1
                if index is len(str):
                    return(0)
                elif not str[index].isdigit():
                    return(0)
            if str[index] is "+":
                negative = False
                index= index+1
                if index is len(str):
                    return(0)
                elif not str[index].isdigit():
                    return(0)
            for ch in str[index:]:
                if ch.isdigit():
                    integer = integer + ch
                else:
                    break
            final = int(integer)
            if negative:
                final = final * -1
            if final < minimum:
                return(minimum)
            elif final > maximum:
                return(maximum)
            else:
                return(final)
            
