class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
        	return n

def get_count(n):
	res = []
	i = 2
	count = n
	while(n >= i*i):
		mark = i
		i += 1
	for i in xrange(mark,1,-1):
		
		
test = Solution()
print test.numSquares(19)