class Solution(object):
    def maxProfit(self, prices):
        maxprofit = 0
        minprice = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - minprice
            if profit > maxprofit:
                maxprofit = profit
            if prices[i] < minprice:
                minprice = prices[i]
        return maxprofit