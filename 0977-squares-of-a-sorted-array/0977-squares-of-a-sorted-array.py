class Solution(object):

    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1

            pos -= 1

        return result