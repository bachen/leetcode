class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
	def combine(self, n, k):
		if k > n:
			return []
		if k == n:
			result = []
			for i in range(1,n+1):
				result +=  [i]
			return result
		

test = Solution()
print test.combine(1,2)