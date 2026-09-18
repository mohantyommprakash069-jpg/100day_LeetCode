class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            second = target-nums[i]
            if second in dic:
                return dic[second],i
            dic[nums[i]]=i

        # for i in range(len(nums)):
        #     second = target - nums[i]
        #     for j in range(i+1,len(nums)):
        #         if second == nums[j]:
        #             return i,j
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j

            
                    
        