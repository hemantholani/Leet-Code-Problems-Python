'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
'''
class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        neg =  (dividend<0) ^ (divisor<0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        print(neg)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend = dividend - temp
                quotient = quotient + i
                i = i*2
                temp = temp * 2
        if neg:
            quotient= quotient*-1
        return min(max(-2147483648, quotient), 2147483647)
            
