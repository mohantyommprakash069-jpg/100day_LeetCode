class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        n = n + k - 1
        r = 2 * k

        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - r + i) // i

        return ans % MOD