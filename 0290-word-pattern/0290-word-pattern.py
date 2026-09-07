class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        p_to_s = {}
        s_to_p = {}

        word = s.split()

        if len(pattern) != len(word):
            return False

        for p, w in zip(pattern, word):

            if p in p_to_s and p_to_s[p] != w:
                return False

            if w in s_to_p and s_to_p[w] != p:
                return False

            p_to_s[p] = w
            s_to_p[w] = p

        return True
