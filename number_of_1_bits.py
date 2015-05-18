class Solution:
	# @param n, an integer
	# @return an integer
	def hammingWeight(self, n):
		if n == 0:
			return 0
		x = n
		count = 0
		if (x%2 == 0):
			count -= 1
		while(x>0):
			x = x >> 1
			if ( x%2 == 1 ) | (x == 0):
				count += 1
		return count

test = Solution()
print test.hammingWeight(50)