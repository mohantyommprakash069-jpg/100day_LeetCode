class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """

        x = int(num)

        while x > 0:
            remain = x % 10

            if remain % 2 != 0:
                return str(x)

            x = x // 10

        return ""