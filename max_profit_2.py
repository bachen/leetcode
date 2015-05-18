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
		diff = [prices[i+1] - prices[i] for i in range(length-1)]
		for i in diff:
			if i > 0:
				profit += i
		return profit

prices1 = [10,20,30,40,30,25,50,10]
test = Solution()

print test.maxProfit(prices1)