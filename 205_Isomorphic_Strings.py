s='abbs'
t='asbb'

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
	def isIsomorphic(self, s, t):
		slength = len(s)
		tlength = len(t) 
		if slength == 0:
			if tlength == 0:
				return True
			else:
				return False

		if tlength == 0:
			if slength == 0:
				return True
			else:
				return False

		a = [([0] * 1) for i in range(slength)]
		ad = {}
		b = [([0] * 1) for j in range(tlength)]
		bd = {}

		for i in range(slength):
			if ad.has_key(s[i]):
				pass
			else:
				ad[s[i]] = i
			a[ad[s[i]]].append(i)

		for j in range(tlength):
			if bd.has_key(t[j]):
				pass
			else:
				bd[t[j]] = j
			b[bd[t[j]]].append(j)

		if a==b:
			return True
		else:
			return False

test = Solution()
print test.isIsomorphic(s,t)

