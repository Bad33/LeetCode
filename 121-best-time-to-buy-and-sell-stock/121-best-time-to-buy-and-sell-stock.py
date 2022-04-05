class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<2:
            return 0
        maxprofit , minstock = float('-inf'),prices[0]
        for p in prices:
            maxprofit = max(maxprofit,p-minstock)
            minstock = min(minstock,p)

            
        return maxprofit
        