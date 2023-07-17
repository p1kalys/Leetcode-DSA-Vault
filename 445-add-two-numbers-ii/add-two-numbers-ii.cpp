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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int>st1,st2;
        while(l1!=nullptr){
            st1.push(l1->val);
            l1=l1->next;
        }
        while(l2!=nullptr){
            st2.push(l2->val);
            l2=l2->next;
        }
        ListNode* result = nullptr;
        int carry=0;
        while(!st1.empty() || !st2.empty() || carry!=0){
            int digit1=!st1.empty() ? st1.top() : 0;
            int digit2=!st2.empty() ? st2.top() : 0;
            int sum=digit1+digit2+carry;
            int digit=sum%10;
            carry=sum/10;

            ListNode* newNode=new ListNode(digit);
            newNode->next=result;
            result=newNode;
            
            if (!st1.empty())
                st1.pop();
            if (!st2.empty())
                st2.pop();
        }
        return result;

    }
};