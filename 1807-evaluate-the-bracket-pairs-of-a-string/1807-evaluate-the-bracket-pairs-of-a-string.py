class Solution(object):
    def evaluate(self, s, knowledge):
        dic = {}

        for item in knowledge:
            dic[item[0]] = item[1]

        result = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""

                while s[i] != ')':
                    key += s[i]
                    i += 1

                if key in dic:
                    result += dic[key]
                else:
                    result += "?"

            else:
                result += s[i]

            i += 1

        return result