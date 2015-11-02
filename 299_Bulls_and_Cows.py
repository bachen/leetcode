class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        countA = 0
        countB = 0
       	length = len(secret)
       	d = {}
       	for i in range(length):
       		if secret[i] == guess[i]:
       			countA += 1
       		if d.has_key(secret[i]):
       			d[secret[i]] += 1
       		else:
       			d[secret[i]] = 1
       	for i in range(length):
       		if d.has_key(guess[i]):
       			if d[guess[i]] > 0:
       				d[guess[i]] -= 1
       				countB += 1
       			else:
       				pass
       	return str(countA)+'A'+str(countB-countA)+'B'

test = Solution()
print test.getHint('1901','9011')