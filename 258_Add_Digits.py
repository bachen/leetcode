class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
    	tmp = num
        while True:
        	res = 0
        	while ((tmp%10 != 0) | (tmp/10 !=0)):
        		res = tmp%10 + res
        		tmp = tmp/10
        	print res
        	if res < 10:
        		return res
        	else:
        		tmp = res
        		continue

test = Solution()
print test.addDigits(10)