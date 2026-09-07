class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        dp = 1
        last = {}

        for ch in s:
            new_dp = 2 * dp - last.get(ch, 0)

            last[ch] = dp
            dp = new_dp % MOD

        return (dp - 1) % MOD