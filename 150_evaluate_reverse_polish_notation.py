class Solution:
	# @param {string[]} tokens
	# @return {integer}
	def evalRPN(self, tokens):
		result = []
		for i in tokens:
			try:
				j = int(i)
				result.append(j)
			except:
				if i == '+':
					a0 = int(result.pop())
					a1 = int(result.pop())
					#print a1 + a0
					result.append(a1 + a0)
				elif i == '-':
					a0 = int(result.pop())
					a1 = int(result.pop())
					#print a1 - a0
					result.append(a1 - a0)
				elif i == '*':
					a0 = int(result.pop())
					a1 = int(result.pop())
					#print a1 * a0
					result.append(a1 * a0)
				elif i == '/':
					a0 = int(result.pop())
					a1 = int(result.pop())
					#print int(a1*1.0 / a0)
					result.append(int(a1*1.0 / a0))
		return result[0]

test = Solution()
print test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])