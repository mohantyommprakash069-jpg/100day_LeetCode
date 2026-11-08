class Solution(object):
    def isAnagram(self, s, t):

        if  len(s) != len(t):
            return False
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in t:
            if i in d:
                d[i]-=1
            else:
                return False
        for key,value in d.items():
            if value!=0:
                return False
        return True
