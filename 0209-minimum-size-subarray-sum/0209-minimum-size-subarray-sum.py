class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        min_length = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                length = right - left + 1

                if length < min_length:
                    min_length = length

                total -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length