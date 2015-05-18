class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		s = s.strip(' ')
		l = s.split(' ')
		result = []
		for i in range(len(l)):
			if l[i] != '':
				result.append(l[i])
		result = result[::-1]
		return ' '.join(result)

test = Solution()

print test.reverseWords('  sdf    sd   ')