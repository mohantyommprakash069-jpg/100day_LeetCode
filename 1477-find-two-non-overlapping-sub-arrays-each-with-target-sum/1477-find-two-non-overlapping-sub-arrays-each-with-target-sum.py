class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        left = 0
        total = 0
        best = n + 1
        ans = n + 1

        minLength = [n + 1] * n

        for right in range(n):
            total += arr[right]

            while total > target and left <= right:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0:
                    ans = min(ans, length + minLength[left - 1])

                best = min(best, length)

            minLength[right] = best

        if ans == n + 1:
            return -1

        return ans