# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head == None):
            return head
        if (head.next == None):
        	return head
        if k == 0:
        	return head
        length = 0
        p = head
        while(p.next):
        	p = p.next
        	length += 1
        length += 1
        p.next = head
        if length > k:
        	mark = length-k-1
        else:
        	if (k%length == 0):
        		p.next = None
        		return head
        	else:
        		mark = length -k%length-1
        pb = head
        print mark
        for i in range(mark):
        	pb = pb.next
        newhead = pb.next
        pb.next = None
        return newhead


listx = []
for i in range(1,6):
	listx.append(ListNode(i))
listx[0].next = listx[1]
listx[1].next = listx[2]


test = Solution()
print test.rotateRight(listx[0],4).val
