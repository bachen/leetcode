class Solution(object):
	def myPow(self, x, n):
	    """
	    :type x: float
	    :type n: int
	    :rtype: float
	    """
	    res = 1
	    if n >= 0:
	        for i in range(n):
	        	res *= x
	        return res
	    else:
	    	for i in range(n):
	        	res *= (1/x)
	        return res
	        
test = Solution()
print test.myPow(0.00001,2147483647)