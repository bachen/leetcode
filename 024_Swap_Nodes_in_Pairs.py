# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def swapPairs(self, head):
		if (head == None):
			return head
		if (head.next == None):
			return head
		cur_p = head
		next_p = head.next
		new_head = next_p
		tmp = next_p.next
		next_p.next = cur_p
		cur_p.next = tmp
		pre = cur_p
		cur_p = cur_p.next
		if cur_p == None:
			return new_head
		next_p = cur_p.next
		while cur_p.next:
			tmp = next_p.next
			next_p.next = cur_p
			cur_p.next = tmp
			pre.next = next_p
			pre = cur_p
			cur_p = cur_p.next
			if cur_p == None:
				break
			next_p = cur_p.next
		return new_head
s=[]
for i in range(2):
	s.append(ListNode(i))
s[0].next = s[1]

test = Solution()

head = test.swapPairs(s[0])
for i in range(2):
	print head.val
	head = head.next
