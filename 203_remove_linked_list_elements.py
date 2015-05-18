# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
	def removeElements(self, head, val):
		if val == None:
			return head
		if head == None:
			return head
		if head.next == None:
			if head.val == val:
				return None
			else:
				return head

		current = head
		phead = None
		
		while current:
			if current.val == val:
				if current.next == None:
					return phead
				else:
					tmp = current.next 
					current.next = None
					current = tmp
			else:
				phead = current
				break

		if phead == None:
			return None
		
		nnode = phead.next
		while nnode:
			if nnode.val == val:
				if nnode.next == None:
					current.next = None
					break
				else:
					nnode = nnode.next
					current.next = nnode
			else:
				if nnode.next == None:
					break
				else:
					tmp = nnode
					nnode = nnode.next
					current = tmp
		return phead

	def print_linked_list(self,head):
		if head == None:
			print None
		if head.next == None:
			print head.val
		print head.val
		cur = head
		nnode = head.next
		while nnode:
			cur = nnode
			print cur.val
			nnode = cur.next

s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(2)
s4 = ListNode(1)
s1.next = s2
s2.next = s3
s3.next = s4

test = Solution()
phead = test.removeElements(s1,1)
test.print_linked_list(phead)
