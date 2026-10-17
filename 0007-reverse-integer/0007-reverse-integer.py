
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        sum1 = 0

        while temp > 0:
            remain = temp % 10
            sum1 = sum1 * 10 + remain
            temp = temp // 10

        if x < 0:
            sum1 = -sum1

        if sum1 < -2**31 or sum1 > 2**31 - 1:
            return 0

        return sum1
