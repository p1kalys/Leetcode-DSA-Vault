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
    ListNode* middleNode(ListNode* head) {
        ListNode* temp=head;
        int a=1;
        while (temp->next!=nullptr){
            temp=temp->next;
            a+=1;
        }
        temp=head;
        a=a/2;
        while (a--){
            temp=temp->next;
        }
        return temp;
    }
};