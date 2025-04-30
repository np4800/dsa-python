class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # # My Way/: Bruteforce
        # ans = {}
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         ans[prices[j] - prices[i]] = [prices[i], prices[j]]
        # print(ans)
        # if ans:
        #     return max(ans)
        # else:
        #     return 0

        # # Optimized Way: One Pass
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
print("Buy and Sell Stock")
print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0