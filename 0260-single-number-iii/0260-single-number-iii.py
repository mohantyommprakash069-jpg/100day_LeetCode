class Solution(object):
    def singleNumber(self, nums):
        ans = 0

        for i in nums:
            ans ^= i

        diff = ans & -ans

        a = 0
        b = 0

        for i in nums:
            if i & diff:
                a ^= i
            else:
                b ^= i

        return a, b