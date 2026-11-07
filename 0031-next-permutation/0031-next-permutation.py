class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        i = n - 2

        # Step 1: Find the pivot
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # Step 2: Find the next greater element
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap using temp
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # Step 4: Reverse the remaining elements
        left = i + 1
        right = n - 1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1