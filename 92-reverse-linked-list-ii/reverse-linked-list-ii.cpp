/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head==NULL || head->next==NULL) return head;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        for (int i = 0; i < left - 1; i++) {
            pre = pre -> next;
        }
        ListNode* cur = pre -> next;
        for (int i = 0; i < right - left; i++) {
            ListNode* forward = cur -> next;
            cur -> next = forward -> next;
            forward -> next = pre -> next;
            pre -> next = forward;

        }
        return dummy -> next;
    }
};