/**
 * Definition for singly-linked list.
**/
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *detectCycle(struct ListNode *head) {
	if (NULL == head)return NULL;
	if (NULL == head->next) return NULL;
	struct ListNode *first = head;
	struct ListNode *second = head->next;
	while(second != NULL){
		if(first == second)break;
		first = first->next;
		second = second->next;
		if (second == NULL)return NULL;
		second = second->next;
		if (second == NULL)return NULL;
	}
	struct ListNode *tmp = head;
	while(second != NULL){
		tmp = second->next;
		second->next = NULL;
		second = tmp;
	}
	first = head;
	while(first != NULL){
		if (first->next == NULL)return first;
		first = first->next;
	}
}
