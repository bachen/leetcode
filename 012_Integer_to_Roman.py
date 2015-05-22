class Solution:
    # @param {integer} num
    # @return {string}
	def intToRoman(self, num):
		tmp = str(num)
		length = len(tmp)
		if length == 0:
			return None
		d = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
		result = []
		for i in range(length):
			if tmp[i] == '0':
				continue
			elif (tmp[i] >= '1') & (tmp[i] < '4'):
				for j in range(int(tmp[i])):
					result.append(d[10**(length - 1 - i)])
				continue
			elif tmp[i] == '4':
				result.append(d[10**(length - 1 -i)])
				result.append(d[5*10**(length - 1 -i)])
				continue
			elif (tmp[i] > '4') & (tmp[i] < '9'):
				result.append(d[5*10**(length - 1 -i)])
				for j in range(int(tmp[i])-5):
					result.append(d[10**(length - 1 -i)])
				continue
			elif tmp[i] == '9':
				result.append(d[10**(length - 1 - i)])
				result.append(d[10**(length -i)])
				continue
		return ''.join(result)

test = Solution()
print test.intToRoman(3999)