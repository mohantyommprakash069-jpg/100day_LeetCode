class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum1 = 0
        temp = x
        while temp > 0:
            remain = temp%10
            sum1+=remain
            temp = temp//10
        if x%sum1 == 0:
            return sum1
        else:
            return -1
        