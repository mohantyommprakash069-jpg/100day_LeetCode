class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # for i in range(len(arr)-1):
        #     if arr[i]<arr[i+1]:
        #         pass
        #     elif arr[i]>arr[i+1]:
        #         return i
        i = 0
        while i<len(arr)-1:
            if arr[i]<arr[i+1]:
                pass
            elif arr[i]>arr[i+1]:
                return i
            i+=1      