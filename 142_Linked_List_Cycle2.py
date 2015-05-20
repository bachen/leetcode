# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
	def hasCycle(self, head):
		if head == None:
			return None
		if head.next == None:
			return None
		tmp = head.next 
		if tmp.next == None:
			return None
		fast_p = tmp.next
		slow_p = head
		while True:
			try:
				if slow_p != fast_p:
					tmp = slow_p
					slow_p = tmp.next
					tmp = fast_p.next
					fast_p = tmp.next
				elif slow_p == fast_p:
					break
			except:
				return None
		while slow_p: #将循环的列表删除，留下linked node成为新链表的最后一个node
			pre = slow_p
			slow_p = pre.next
			pre.next = None
		slow_p = head 
		while slow_p:
			pre = slow_p
			slow_p = slow_p.next
			if slow_p == None:
				return pre

s=[]
for i in range(5):
	s.append(ListNode(i))
s[0].next = s[1]
s[1].next = s[2]
s[2].next = s[1]
test = Solution()
print test.hasCycle(s[0])