
class Solution(object):
    def mostFrequentPrime(self, mat):
        m = len(mat)
        n = len(mat[0])

        d = {}

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        def isPrime(num):
            if num < 2:
                return False

            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1

            return True

        for i in range(m):
            for j in range(n):

                for dx, dy in directions:

                    x = i
                    y = j
                    num = 0

                    while 0 <= x < m and 0 <= y < n:

                        num = num * 10 + mat[x][y]

                        if num > 10 and isPrime(num):
                            d[num] = d.get(num, 0) + 1

                        x += dx
                        y += dy

        if not d:
            return -1

        ans = -1
        maxi = 0

        for num in d:
            if d[num] > maxi:
                maxi = d[num]
                ans = num

            elif d[num] == maxi:
                ans = max(ans, num)

        return ans
