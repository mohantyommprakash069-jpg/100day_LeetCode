# class Solution(object):
#     def maxProduct(self, nums):
#         max1 = nums[0]

#         for i in range(len(nums)):
#             product = 1

#             for j in range(i, len(nums)):
#                 product *= nums[j]
#                 max1 = max(max1, product)

#         return max1
class Solution(object):
    def maxProduct(self, nums):
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxi, mini = mini, maxi

            maxi = max(nums[i], maxi * nums[i])
            mini = min(nums[i], mini * nums[i])

            ans = max(ans, maxi)

        return ans