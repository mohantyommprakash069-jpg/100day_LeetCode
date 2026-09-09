class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        seen = {}

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

        seen = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        result = ""

        for key, val in seen:
            result += key * val

        return result