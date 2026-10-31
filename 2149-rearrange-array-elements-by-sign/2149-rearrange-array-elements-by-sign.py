# class Solution(object):
#     def rearrangeArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         nums1=[]
#         nums2 = []
#         nums3 = []
#         for i in range(len(nums)):
#             if nums[i]>0:
#                 nums2.append(nums[i])
#             else:
#                 nums3.append(nums[i])
#         for i in range((len(nums)//2)):
#             nums1.append(nums2[i])
#             nums1.append(nums3[i])
#         return nums1
class Solution(object):
    def rearrangeArray(self,nums):
        result = [0]*len(nums)
        pos= 0
        neg = 1
        for i in range(len(nums)):
            if nums[i]>0:
                result[pos] = nums[i]
                pos+=2
            else:
                result[neg] = nums[i]
                neg+=2
        return result