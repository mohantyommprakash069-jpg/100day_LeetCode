class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        sum1 = 0
        mod = 1337
        for i in b:
            sum1 = sum1*10+i
        return pow(a, sum1, mod)