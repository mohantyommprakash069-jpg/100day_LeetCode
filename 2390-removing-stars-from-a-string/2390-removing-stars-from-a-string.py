class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)):
            if s[i] ==  '*':
                if result:
                    result.pop()
            else:
                result.append(s[i])
        return ''.join(result)