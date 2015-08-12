class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        length = len(digits)
        res = []
        if digits[0] == '-':
        	tmp = 0
        	for i in xrange(1,length):
        		tmp = digits[i] + tmp * 10
        	tmp = str(-tmp + 1)
        	res.append('-')
        	for i in xrange(1,len(tmp)):
        		res.append(int(tmp[i]))
       	elif digits[0] == '+':
       		tmp = 0
       		for i in xrange(1,length):
       			tmp = digits[i] + tmp * 10
       		tmp = str(tmp+1)
       		for i in xrange(len(tmp)-1):
       			res.append(int(tmp[i]))
       	else:
       		tmp = 0
       		for i in xrange(length):
       			tmp = digits[i] + tmp * 10
       		print tmp
       		tmp = str(tmp+1)
       		for i in xrange(len(tmp)):
       			res.append(int(tmp[i]))
       	return res

test = Solution()
print test.plusOne([9])