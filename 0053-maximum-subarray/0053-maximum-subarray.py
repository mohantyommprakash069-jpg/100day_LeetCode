class Solution:
    def maxSubArray(self, nums):
        count = 0
        max1 = nums[0]
        left = 0

        for right in range(len(nums)):
            count += nums[right]

            max1 = max(max1, count)

            while count < 0:
                count -= nums[left]
                left += 1

        return max1
# class Solution(object):
#     def maxSubArray(self, nums):
#         count = 0
#         max1 = nums[0]

#         for i in range(len(nums)):
#             count += nums[i]

#             max1 = max(count, max1)

#             if count < 0:
#                 count = 0

#         return max1