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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int>l1;
        for(int i=0; i<lists.size(); i++){
            while (lists[i]!=NULL) {
                l1.push_back(lists[i]->val);
                lists[i]=lists[i]->next;
            }
        }
        sort(l1.begin(),l1.end());
        ListNode* res = new ListNode(0);
        ListNode* ans = res;
        for (auto i: l1) {
            ListNode* temp = new ListNode(i);
            res -> next = temp;
            res = res->next;
        }
        res->next = nullptr;
        return ans->next;
    }
};