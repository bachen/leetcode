class Solution:
	# @param {string} s
	# @return {integer}
	def myAtoi(self, s):
		s = s.lstrip(' ')
		length = len(s)
		if length == 0:
			return 0
		if length == 1:
			if s[0].isdigit():
				return int(s[0])
			else:
				return 0
		result = []
		flag = False
		if (s[0] == '+') | (s[0] == '-'):
			flag = True
			for i in range(1,length):
				if s[i].isdigit():
					result.append(s[i])
				else:
					break
		elif s[0].isdigit():
			flag = False
			for i in range(1,length):
				if s[i].isdigit():
					result.append(s[i])
				else:
					break
		else:
			return 0
		if (result == []) & (flag == True):
			return 0
		number = int(s[0] + ''.join(result))
		if number > (2**31 -1):
			return (2**31 -1)
		if number < -(2**31):
			return -(2**31)
		return number

test = Solution()
print test.myAtoi('   ')
print test.myAtoi(' +dhsi')
print test.myAtoi(' -1hiuas')
print test.myAtoi('   201nos')
print test.myAtoi('-2147483649')