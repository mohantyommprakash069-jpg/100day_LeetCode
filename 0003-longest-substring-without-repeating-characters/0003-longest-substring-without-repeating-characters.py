class Solution:
    def lengthOfLongestSubstring(self, s):
        count = 0
        result = set()
        max1 = 0
        i = 0

        for j in range(len(s)):
            while s[j] in result:
                result.remove(s[i])
                i += 1

            result.add(s[j])
            count = j - i + 1
            max1 = max(count, max1)

        return max1