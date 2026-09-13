class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        low = prices[0]

        for price in prices:
            if price - low > output:
                output = price - low
            if price < low:
                low = price
        
        return output
        