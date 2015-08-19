class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
    	if num < 1:
    		return False
    	if num == 1:
    		return True
        if (num%2 != 0) & (num%3 != 0) & (num%5 != 0):
        	return False
        while(num%2 == 0):
        	num = num/2
        while(num%3 == 0):
        	num = num/3
        while(num%5 == 0):
        	num = num/5
        if num == 1:
        	return True
        else:
        	return False

test = Solution()
print test.isUgly(0)