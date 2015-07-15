# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        current = node
        nnode = current.next
        while(current.next != None):
            current.val = nnode.val
            pre = current
            current = nnode
            nnode = current.next
        pre.next = None