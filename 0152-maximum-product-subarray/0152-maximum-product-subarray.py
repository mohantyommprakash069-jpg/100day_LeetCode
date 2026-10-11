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
        product = 1

        for i in range(len(nums)):
            product *= nums[i]
            maxi = max(maxi, product)

            if product == 0:
                product = 1

        product = 1

        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            maxi = max(maxi, product)

            if product == 0:
                product = 1

        return maxi