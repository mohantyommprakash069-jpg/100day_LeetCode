class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        min1=float('inf')
        man2=float('inf')
        for i in range(len(prices)):
            if prices[i]<min1:
                min2 = min1
                min1 = prices[i]
            elif prices[i] < min2:
                min2 = prices[i]
        if money>=min1+min2:
            return money-(min1+min2)
        else:
            return money