# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        pre = head
        nex1 = head
        tmp = n
        count = 0
        while(tmp > 0):
        	if pre.next == None:
        		if count < n-1:
        			return head
        		else:
        			node = head.next
        			head.next = None
        			return node
        	pre = pre.next
        	tmp -= 1
        	count += 1
        while True:
        	if pre.next == None:
        		break
        	nex1 = nex1.next
        	pre = pre.next
        nex2 = nex1.next.next
        nex1.next = nex2
        return head

lnode = []

[lnode.append(ListNode(i)) for i in range(1)]
'''
[lnode.append(ListNode(i)) for i in range(5)]
lnode[0].next = lnode[1]
lnode[1].next = lnode[2]
lnode[2].next = lnode[3]
lnode[3].next = lnode[4]

print lnode[0].val
print lnode[0].next.val
print lnode[0].next.next.val
print lnode[0].next.next.next.val
print lnode[0].next.next.next.next.val
'''
test = Solution()
node = test.removeNthFromEnd(lnode[0],1)
print node

