class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        result = 0
        if prices == []:
            return result
        
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right += 1
            elif prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                result = max(result, temp)
                right += 1
        
        return result