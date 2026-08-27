class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        arr=[0]*(2*n)
        for i in range(n):
            arr[i]=nums[i]
            arr[i+n]=nums[i]
        return arr
        