class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
        	return '1'
        pre = ['1']
        cur = []
        mark = pre[0]
        count = 0
        for j in range(n-1):
            for i in pre:
            	if i == mark:
            		count += 1
            	else:
            		cur.append(str(count))
            		cur.append(mark)
            		mark = i
            		count = 1
            cur.append(str(count))
            cur.append(mark)
            pre = cur
            cur = []
            count = 0
            mark = pre[0]
        #return pre
        return ''.join(pre)

test = Solution()
print test.countAndSay(6)