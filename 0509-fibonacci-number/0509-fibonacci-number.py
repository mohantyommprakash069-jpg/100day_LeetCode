class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fibn(n):
            if n<=1:
                return n
            else:
                return fibn(n-1) + fibn(n-2)
        return fibn(n)
            