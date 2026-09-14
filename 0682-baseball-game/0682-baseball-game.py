class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        sum1=0
        result=[]
        for i in operations:
            if i == '+':
                result.append(result[-1] + result[-2])
            elif i == 'D':
                result.append(result[-1]*2)
            elif i == 'C':
                result.pop()
            else:
                result.append(int(i))
        for j in result:
            sum1+=j
        return sum1


