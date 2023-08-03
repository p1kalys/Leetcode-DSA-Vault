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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp=head;
        if(n==0) return head;

        int len=0;
        while(temp!=NULL){
            temp=temp->next;
            len++;
        }
        if (len<n) return NULL;

        if(len-n == 0){
            head=head->next;
            return head;
        }
        temp=head;
        ListNode* prev=head;
        for(int i=0; i<len-n; i++){
            prev=temp;
            temp=temp->next;
        }
        prev->next=temp->next;
        return head;
    }
};