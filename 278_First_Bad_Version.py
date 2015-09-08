# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	if version > 1:
		return True
	else:
		return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return findbadversion(1,n)

def findbadversion(start,end):
	if (start+1) >= end:
		if isBadVersion(start):
			return start
		else:
			return end
	mid = (start + end)/2
	if isBadVersion(mid):
		return findbadversion(start,mid)
	else:
		return findbadversion(mid,end)

test = Solution()
print test.firstBadVersion(4)