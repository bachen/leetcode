class Solution:
	# @param {integer} x
	# @return {integer}
	def reverse(self, x):
		s = str(x)
		length = len(s)
		if (length == 0) | (length == 1):
			return x
		if s[0].isdigit():
			tmp = list(s)
			tmp = tmp[::-1]
			result = int(''.join(tmp))
			#print result
		else:
			tmp = list(s)
			tmp = tmp[::-1]
			signal = tmp.pop()
			result = int(signal + ''.join(tmp))

		if result > 2**31:
			return 0
		elif result <= -(2**31):
			return 0
		else:
			return result

test = Solution()
print test.reverse(123)
print test.reverse(-123)
print test.reverse(-2147483648)
print test.reverse(1563847412)
print test.reverse(1534236469)