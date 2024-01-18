class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        previous, current = 1,1
        for i in range(2, n+1):
            temp     = current
            current  = previous + current
            previous = temp
        return current
