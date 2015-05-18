class Solution:
	def convert(self, s, numRows):
		length = len(s)
		if length < numRows:
			return s
		if numRows == 1:
			return s
		if numRows == 0:
			return s
		m = length / numRows
		n = length % numRows
		if n > 0:
			m = m + 1
		result = []
		for i in range(numRows):
			for j in range(m):
				left = j*(2*numRows-2) - i
				right = j*(2*numRows-2) + i
				if (left >= 0) & (left < length):
					if left in result:
						pass
					else:
						#print left
						result.append(left)
				if (right < length) & (right > 0):
					if right in result:
						continue
					else:
						#print right
						result.append(right)
		#print result
		new_string = []
		for i in range(len(result)):
			new_string.append(s[result[i]])
		#print new_string
		new_s = ''.join(new_string)
		return new_s

test = Solution()
print test.convert('ABCDEFSYGSKAY',10)
print test.convert('A',1)
print test.convert('ABS',1)
print test.convert('',0)
print test.convert('ABCD',3)
print test.convert('ABCD',2)
print test.convert('ABCDE',4)