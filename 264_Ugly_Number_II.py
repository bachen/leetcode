class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        res = [0]*n
        res[0]=1
        m2=0
        m3=0
        m5=0
        for i in range(1,n):
        	pre = res[i-1]
        	while (res[m2]*2<=pre):
        		m2 += 1
        	while (res[m3]*3<=pre):
        		m3 += 1
        	while (res[m5]*5<=pre):
        		m5 += 1
        	c2 = res[m2]*2
        	c3 = res[m3]*3
        	c5 = res[m5]*5
        	res[i] = min(c2,c3,c5)
        return res

test = Solution()
print test.nthUglyNumber(1500)