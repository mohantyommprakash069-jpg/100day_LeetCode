class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        for i in range(n + 1):
            x = i
            y = []
            
            while x > 0:
                r = x % 2
                y.append(r)
                x = x // 2

            count = 0

            for j in y:
                if j == 1:
                    count += 1

            result.append(count)

        return result