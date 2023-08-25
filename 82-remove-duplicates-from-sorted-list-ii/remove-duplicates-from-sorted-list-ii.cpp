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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* a = head, *b = head,*c, *ans;
        unordered_map<int, int>mp;
        c = new ListNode(0);
        ans=c;

        while (a) {
            mp[a -> val]++;
            a = a -> next;
        }

        while (b) {
            if (mp[b->val] == 1) {
                c -> next = b;
                c = c -> next;
            }
            b = b -> next;
        }
        c -> next = nullptr;
        return ans -> next;
    }
};