# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        helper = ListNode(0)
        helper.next = head
        cur2=head.next
        while(cur2 != None):
            cur1 = helper
            while (cur1 != None & cur1.next.val > cur2.val):
                cur1 = cur1.next
            tmp = cur2.next
            cur2.next = cur1.next
            cur2 = tmp
        return helper.next
'''
public ListNode insertionSortList(ListNode head) {
    if(head == null)
        return null;
    ListNode helper = new ListNode(0);
    ListNode pre = helper;
    ListNode cur = head;
    while(cur!=null)
    {
        ListNode next = cur.next;
        pre = helper;
        while(pre.next!=null && pre.next.val<=cur.val)
        {
            pre = pre.next;
        }
        cur.next = pre.next;
        pre.next = cur;
        cur = next;
    }
    return helper.next;
}
'''

s0 = ListNode(3)
s1 = ListNode(2)
s2 = ListNode(4)


s0.next = s1
s1.next = s2


test = Solution()
new_head = test.insertionSortList(s0)
print new_head.val
print new_head.next.val
print new_head.next.next.val

