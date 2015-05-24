class Solution:
    # @param {integer[]} prices
    # @return {integer}
	def maxProfit(self, prices):
		length = len(prices)
		if length == 0:
			return 0
		if length == 1:
			return 0
		profit = 0
		max_profit = 0
		for i in range(1,length):
			if profit > max_profit:
				max_profit = profit
			profit += (prices[i] - prices[i-1])
			if profit < 0:
				profit = 0
		if profit > max_profit:
			max_profit = profit
		return max_profit

prices1 = [6,1,3,2,4,7]
test = Solution()

print test.maxProfit(prices1)