# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         # count =0 
#         # for i in range(len(nums)):
#         #     for j in range(i,len(nums)):

#         #         sum1 = 0
#         #         for x in range(i,j+1):
#         #             sum1+=nums[x]
#         #         if sum1 == k:
#         #             count+=1

#         # return count
#         # count = 0
#         # for i in range(len(nums)):
#         #     sum1 = 0
#         #     for j in range(i,len(nums)):
#         #         sum1+=nums[j]
#         #         if sum1 == k:
#         #             count+=1
#         # return count




class Solution(object):
    def subarraySum(self, nums, k):

        prefix = 0
        count = 0
        d = {0: 1}

        for i in range(len(nums)):
            prefix += nums[i]

            diff = prefix - k

            if diff in d:
                count += d[diff]

            if prefix in d:
                d[prefix] += 1
            else:
                d[prefix] = 1

        return count
