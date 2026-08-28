class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        median=0
        mid=len(nums3)//2
        if len(nums3)%2 == 0:
            median=float(nums3[mid-1]+nums3[mid])/2
            
        else:
            median=float(nums3[mid])
           
        return median
