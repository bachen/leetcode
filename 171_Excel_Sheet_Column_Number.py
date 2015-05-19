class Solution:
    # @param {string} s
    # @return {integer}
	def titleToNumber(self, s):
		length = len(s)
		mark = ord('A') - 1
		result = 0
		for i in range(length):
			i = i + 1
			result = result + (ord(s[-i]) - mark)*(26**(i-1))
		return result

test = Solution()
print test.titleToNumber('AZ')