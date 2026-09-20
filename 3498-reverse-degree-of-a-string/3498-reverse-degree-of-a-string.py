class Solution(object):

    def reverseDegree(self, s):

        """
        :type s: str
        :rtype: int
        """

        sum1 = 0

        for i in range(len(s)):

            x = (123-ord(s[i]))
            
            z = x*(i+1)

            sum1 += z

        return sum1