class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
    	if n <= 0:
    		return False
    	if n == 1:
    		return True
    	flag = judge(n)
    	return flag

def judge(n):
	a,b = n%2,n/2
	if a == 0:
		if b == 1:
			return True
		else:
			return judge(b)
	else:
		return False

if __name__=='__main__':
	test=Solution()
	print test.isPowerOfTwo(0)
	print test.isPowerOfTwo(256)