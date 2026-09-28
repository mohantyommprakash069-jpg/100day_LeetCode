class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def getMax(nums, length):
            stack = []
            remove = len(nums) - length

            for num in nums:
                while stack and remove > 0 and stack[-1] < num:
                    stack.pop()
                    remove -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            ans = []

            while a or b:
                if a > b:
                    ans.append(a.pop(0))
                else:
                    ans.append(b.pop(0))

            return ans

        ans = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            a = getMax(nums1, i)
            b = getMax(nums2, k - i)

            candidate = merge(a[:], b[:])

            if candidate > ans:
                ans = candidate

        return ans