# class Solution(object):
#     def peakIndexInMountainArray(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
#         # for i in range(len(arr)-1):
#         #     if arr[i]<arr[i+1]:
#         #         pass
#         #     elif arr[i]>arr[i+1]:
#         #         return i
#         i = 0
#         while i<len(arr)-1:
#             if arr[i]<arr[i+1]:
#                 pass
#             elif arr[i]>arr[i+1]:
#                 return i
#             i+=1      
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left