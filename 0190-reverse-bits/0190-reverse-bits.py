class Solution(object):
    def reverseBits(self, n):
        result = []

        for i in range(32):
            remain = n % 2
            result.append(remain)
            n = n // 2

        sum1 = 0
        for i in range(32):
            sum1 += result[i] * (2 ** (31 - i))

        return sum1
