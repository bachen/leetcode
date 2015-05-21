# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def deleteDuplicates(self, head):
		if (head == None):
			return head
		if (head.next == None):
			return head
		cur = head.next
		node = head
		while cur:
			if cur.val == node.val:
				node.next = None
				cur = cur.next
			else:
				node.next = cur
				node = cur
				cur = cur.next
		return head

test = Solution()
t = [1,2,2]
s =[]
for i in t:
	s.append(ListNode(i))
s[0].next = s[1]
s[1].next = s[2]
test.deleteDuplicates(s[0])
print s[1].next