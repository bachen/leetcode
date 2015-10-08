class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l1 = len(pattern)
        d1 = {}
        d2 = {}
        flag = True
        words = string.split(' ')
        l2 = len(words)
        if l1 != l2:
        	return False
        for i in range(l1):
        	if d1.has_key(pattern[i]):
        		if d1[pattern[i]] != words[i]:
        			flag = False
        			return flag
        	else:
        		d1[pattern[i]] = words[i]
        	if d2.has_key(words[i]):
        		if d2[words[i]] != pattern[i]:
        			flag = False
        			return flag
        	else:
        		d2[words[i]] = pattern[i]
        return flag

test = Solution()
print test.wordPattern("abba","dog dog dog dog")