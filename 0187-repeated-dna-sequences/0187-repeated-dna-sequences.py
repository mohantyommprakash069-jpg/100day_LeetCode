class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dic = {}
        ans = []

        for i in range(len(s) - 9):
            seq = s[i:i+10]

            if seq in dic:
                if dic[seq] == 1:
                    ans.append(seq)
                dic[seq] += 1
            else:
                dic[seq] = 1

        return ans