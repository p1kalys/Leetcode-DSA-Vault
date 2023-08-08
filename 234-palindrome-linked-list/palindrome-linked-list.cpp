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
ListNode* reverse(ListNode* head){
    ListNode* pre=NULL;
    ListNode* next=NULL;
    while (head!=NULL){
        next=head->next;
        head->next=pre;
        pre=head;
        head=next;
    }
    return pre;
}
    bool isPalindrome(ListNode* head) {
        if(!head)   return true;
        if(!head->next) return true;
        ListNode* fast=head, *slow=head;
        while(fast->next!=NULL && fast->next->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        slow->next=reverse(slow->next);
        slow=slow->next;
        ListNode* dummy=head;
        while(slow!=NULL){
            if(slow->val != dummy->val){
                return false;
            }
            slow=slow->next;
            dummy=dummy->next;
        }
        return true;
    }
};