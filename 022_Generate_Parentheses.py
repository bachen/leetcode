class Solution:
    # @param {integer} n
    # @return {string[]}
	def generateParenthesis(self, n):
		result = []
		if 0 >= n:
			return result
		n0 = n
		n1 = n
		generate(result,n0,n1,'')
		return result

def generate(result,n0,n1,s):
	if (n0 == 0) & (n1 == 0):
		result.append(s)
	if n0 > 0:
		s1 = s +'('
		generate(result,n0-1,n1,s1)
	if (n1 > 0) & (n1 > n0):
		s2 = s +')'
		generate(result,n0,n1-1,s2)

test = Solution()
print test.generateParenthesis(4)
