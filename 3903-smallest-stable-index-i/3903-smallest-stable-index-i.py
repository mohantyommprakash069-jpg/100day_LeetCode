class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Minimum from i to n-1
        right_min = [0] * n
        right_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])

        # Maximum from 0 to i
        left_max = nums[0]

        for i in range(n):
            left_max = max(left_max, nums[i])

            instability = left_max - right_min[i]

            if instability <= k:
                return i

        return -1