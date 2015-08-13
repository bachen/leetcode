class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        res = s.split(' ')
        length = len(res)
        for i in xrange(length-1,-1,-1):
        	if res[i] != '':
        		return len(res[i])
        return 0

test = Solution()
print test.lengthOfLastWord('a')