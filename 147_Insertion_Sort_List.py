# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if (head == None):
        	return head
        if (head.next == None):
        	return head
        h1 = head
        h2 = head.next
        h1.next = None
        new_head = head
        if h2.val >= h1.val:
            h1.next = h2
            new_head = h1
            h2 = h2.next
        else:
            h2.next = h1
            new_head = h2
            h2 = h2.next
        while(h2):
            #print h2.val
            tmp1 = h2.next
            h1 = new_head
            #print h1.val
            if h1.val >= h2.val:
                h2.next = h1
                new_head = h2
            else:
                while(h1):
                    if (h2.val >= h1.val) & (h1.next == None):
                        h1.next = h2
                        break
                    elif h1.next != None:
                        if (h2.val >= h1.val) & (h1.next.val >= h2.val):
                            tmp2 = h1.next
                            h1.next = h2
                            h2.next = tmp2
                            break
                        else:
                        	h1 = h1.next
            h2 = tmp1
        return new_head

s0 = ListNode(1)
s1 = ListNode(1)
#s2 = ListNode(1)


s0.next = s1
#s1.next = s2


test = Solution()
new_head = test.insertionSortList(s0)
print new_head.val
print new_head.next.val
#print new_head.next.next.val

