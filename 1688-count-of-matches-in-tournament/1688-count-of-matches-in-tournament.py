class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum1 = 0
         

        while n > 1:
            if n % 2 == 0:
                sum1 += n // 2
                n = n // 2
            else:
                sum1 += (n - 1) // 2
                n = ((n - 1) // 2) + 1

        return sum1
        