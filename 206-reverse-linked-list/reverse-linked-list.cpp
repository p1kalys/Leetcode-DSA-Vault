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
    ListNode* reverseList(ListNode* head) {
        if (head==nullptr){
            return head;
        }
        else if (head->next==nullptr){
            return head;
        }
        else{
            ListNode* temp=nullptr;
            ListNode* nextnode=nullptr;
            while (head!=nullptr){
                nextnode=head->next;
                head->next=temp;
                temp=head;
                head=nextnode;
            }
            return temp;
        }
    }
};