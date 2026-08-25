class Solution(object):
    def isValid(self, s):
        para=[]
        for i in s:
            if i == '(':
                para.append(')')
            elif i == '{':
                para.append('}')
            elif i == '[':
                para.append(']')
            else:
                if not para or para.pop() != i:
                    return False

        return len(para) == 0
        