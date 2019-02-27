'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        stairs = [0,1,2]
        for i in range(3,(n+1)):
            stairs.append(stairs[i-1] + stairs[i-2])
        return stairs[n]
