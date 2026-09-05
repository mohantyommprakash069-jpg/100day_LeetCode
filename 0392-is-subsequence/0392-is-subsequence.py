class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        j = 0

        for i in s:
            while j < len(t):
                if i == t[j]:
                    j += 1
                    break
                j += 1
            else:
                return False

        return True