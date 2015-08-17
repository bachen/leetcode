/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode *nex = node;
    struct ListNode *pre = node;
    while(node->next != NULL){
        nex = node->next;
        node->val = nex->val;
        pre = node;
        node = nex;
    }
    pre->next = NULL;
}