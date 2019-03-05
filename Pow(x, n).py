'''
Implement pow(x, n), which calculates x raised to the power n (xn).
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1 :
            return x
        if n < 0:
            return self.myPow(1/x,-n)
        else:
            if n%2==0:
                return self.myPow(x*x,n/2)
            else:
                return self.myPow(x*x,(n-1)/2)*x
            
