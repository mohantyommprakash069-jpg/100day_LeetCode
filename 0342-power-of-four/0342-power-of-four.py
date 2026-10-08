class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False

        count = 0
        while (n&1) == 0:
            n = n>>1
            count+=1
        return n==1 and count % 2 == 0