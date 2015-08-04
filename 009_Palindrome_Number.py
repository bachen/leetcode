class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
        	return False
        div1 = 1
        count = 1
        tmp = x
        while(tmp/10):
        	tmp = tmp/10
        	div1 *= 10
        	count += 1
        tmp1 = x
        tmp2 = x
        for i in range(count/2):
        	m1 = tmp1/div1
        	tmp1 = tmp1%div1
        	div1 = div1/10
        	m2 = tmp2%10
        	tmp2 = tmp2/10
        	if m1 != m2:
        		return False
        return True

test = Solution()
print test.isPalindrome(11)