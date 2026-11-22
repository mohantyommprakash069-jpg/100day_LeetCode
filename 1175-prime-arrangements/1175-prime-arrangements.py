class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = 0
        non_prime = 0
        for i in range(1,n+1):
            count = 0
            for j in range(1,i+1):
                if i%j == 0:
                    count+=1
            if count == 2:
                prime+=1
            else:
                non_prime+=1
        p = 1
        for i in range(1,prime+1):
            p*=i
        np = 1
        for i in range(1,non_prime+1):
            np*=i
        return (np*p)%(10**9+7)
        