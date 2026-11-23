
class Solution(object):
    def smallestValue(self, n):
        while True:
            total = 0
            num = n

            for i in range(2, num + 1):
                while num % i == 0:
                    total += i
                    num //= i

            if total == n:
                return n

            n = total
