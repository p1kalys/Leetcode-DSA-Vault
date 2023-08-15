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
    void insert(ListNode *&tail,int data){
        ListNode *temp=new ListNode (data);
        tail->next=temp;
        tail=temp;
    }

    ListNode* partition(ListNode* head, int x) {
        ListNode* big= new ListNode(-1);
        ListNode* bigt=big;
        ListNode* small=new ListNode(-1);
        ListNode* smallt=small;

        ListNode *temp=head;
        while(temp!=NULL){
        if(temp->val < x){
          insert(smallt,temp->val);
        }
        else{
            insert(bigt,temp->val);
        }
        temp=temp->next;
        }
      
        if(small->next==NULL){
            return big->next;
        }

        smallt->next=big->next;
        ListNode *ans=small->next;
        delete small;
        delete  big;
        return ans;
    }
};