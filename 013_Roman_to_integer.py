class Solution:
    # @param {string} s
    # @return {integer} 1-3999
	def romanToInt(self, s):
		length = len(s)
		if length == 0:
			return None
		d = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
		result = 0
		if length == 1:
			return d[s[0]]
		i = 0
		while (i < (length-1)):
			if d[s[i]] < d[s[i+1]]:
				#print i
				result += (d[s[i+1]] - d[s[i]])
				i += 2
			else:
				result += d[s[i]]
				i += 1
				#print i
			if (i == (length -1)):
				result += d[s[i]]
		return result

test = Solution()
print test.romanToInt('MMMCMXCIX')
print test.romanToInt('MDCXCV')
print test.romanToInt('MCMLXXXIV') #1984
print test.romanToInt('MCMXCVI')