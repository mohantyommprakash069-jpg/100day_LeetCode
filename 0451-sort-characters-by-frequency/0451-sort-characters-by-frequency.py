class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        result = sorted(d.items(), key=lambda x: x[1], reverse=True)

        s = ""
        for key, value in result:
            s += key * value

        return s