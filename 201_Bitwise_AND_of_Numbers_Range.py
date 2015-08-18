class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while(m!=n):
            m = m>>1
            n = n>>1
            count += 1
        return m << count

    def rangeBitwiseAnd1(self, m, n):
        count = 0
        while(n>m):
            n = n&(n-1)
        return m&n

test = Solution()
print test.rangeBitwiseAnd1(13,15)