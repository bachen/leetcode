class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        count = 1
        length = len(s)
        if length == 0:
        	return 0
        if length == 1:
        	return 1
        if length == 2:
        	if s[0] == s[1]:
        		return 2
        	else:
        		return 1
        for i in range(2,length):
        	for j in range(1,i):
        		if s[i + j - 1] == s[i - j]:
                    count += 1
