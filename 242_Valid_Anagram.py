class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        len_s = len(s)
        len_t = len(t)
        if len_t != len_s:
        	return False
        ds = {}
        for i in range(len_s):
        	if ds.has_key(s[i]):
        		ds[s[i]] += 1
        	else:
        		ds[s[i]] = 1
        dt = {}
        for i in range(len_t):
        	if dt.has_key(t[i]):
        		dt[t[i]] += 1
        	else:
        		dt[t[i]] = 1
        if dt == ds:
        	return True
        else:
        	return False

test = Solution()
print test.isAnagram('anagram','nagaram')