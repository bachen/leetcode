class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2:
        	return 0
        prime = [True]*n
        prime[0] = False
        prime[1] = False

        limit = math.sqrt(n)
        i = 2
        while (i < limit):
        	if prime[i]:
        		for j in xrange(i*i,n,i):
        			prime[j] = False
        	i = i + 1

        count = 0
        for i in range(n):
        	if prime[i]:
        		count = count + 1
        return count