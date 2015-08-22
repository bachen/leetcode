class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber1(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
    	print a,b
        return [1, -1][a + b > b + a]

    def largestNumber(self,num):


test =Solution()
print test.largestNumber([5,2,95,30])