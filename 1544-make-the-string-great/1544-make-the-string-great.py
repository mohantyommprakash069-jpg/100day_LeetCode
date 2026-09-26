class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

       

        for i in range(len(s)):
            if s[i].isupper():
                if result and result[-1] == s[i].lower():
                    result.pop()
                else:
                    result.append(s[i])
            else:
                if result and result[-1] == s[i].upper():
                    result.pop()
                else:
                    result.append(s[i])

        return "".join(result)