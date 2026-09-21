class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * k

        dp = [0] * k

        for i in range(n):
            new = [0] * k
            new[nums[i] % k] += 1

            for r in range(k):
                new[(r * nums[i]) % k] += dp[r]

            dp = new

            for r in range(k):
                result[r] += dp[r]

        return result