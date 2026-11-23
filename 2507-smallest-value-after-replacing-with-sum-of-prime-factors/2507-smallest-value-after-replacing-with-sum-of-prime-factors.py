
class Solution(object):
    def smallestValue(self, n):
       while True:
        num = n
        total = 0
        for i in range(2,n+1):
            while num%i == 0:
                total+=i
                num//=i
        if total == n:
            return n
        n = total