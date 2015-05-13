# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None:
        	return head
        if head.next == None:
            return head
        pnode = head
        nnode = head.next
        head.next = None
        while nnode:
        	tmp = nnode.next
        	nnode.next = pnode
        	pnode = nnode
        	nnode = tmp
        return pnode