class Solution:
	def lengthOfLongestSubstring(self, s):
		length = len(s)
		start,end = 0,0
		d = {}
		count = 0
		if length == 0:
			return 0
		if length == 1:
			return 1
		while True:
			if d.has_key(s[end]):
				count = max(count,(end - start))
				start = d[s[end]] + 1
				d = {}
				d[s[start]] = start
				end = start + 1
			else:
				d[s[end]] = end
				end += 1
			if (end >= length):
				count = max(count,(end - start))
				break
		return count

test = Solution()
print test.lengthOfLongestSubstring('au')
print test.lengthOfLongestSubstring('pwwkew')
print test.lengthOfLongestSubstring('aabcashobuahiohis')