class Solution(object):
    def summaryRanges(self, nums):
        result = []
        
        if not nums:
            return result
        
        start = nums[0]

        for i in range(len(nums) - 1):
            
            # Consecutive numbers
            if nums[i] + 1 == nums[i + 1]:
                continue
            
            # Range ended
            if start == nums[i]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[i]))
            
            # Start new range
            start = nums[i + 1]

        # Add the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))

        return result