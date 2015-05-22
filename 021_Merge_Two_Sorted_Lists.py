# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
	def mergeTwoLists(self, l1, l2):
		if (l1 == None) & (l2 == None):
			return None
		if l1 == None:
			return l2
		if l2 == None:
			return l1
		cur1 = l1
		cur2 = l2
		if (cur1.val > cur2.val):
			head = cur2
			keep = cur2
			cur2 = cur2.next
		else:
			head = cur1
			keep = cur1
			cur1 = cur1.next
		while ((cur1 != None) & (cur2 != None)):
			if (cur1.val > cur2.val):
				keep.next = cur2
				keep = cur2
				cur2 = cur2.next
			else:
				keep.next = cur1
				keep = cur1
				cur1 = cur1.next
		if (cur1 != None):
			keep.next = cur1
		elif (cur2 != None):
			keep.next = cur2
		return head