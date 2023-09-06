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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int len = 0;
        vector<ListNode*> res;
        ListNode* cur = head;
        while (cur) {
            cur = cur->next;
            len++;
        }

        int base_len = len / k;
        int rem = len % k;
        cur = head;
        while (cur) {
            ListNode* temp = cur;
            int t = base_len;

            if (rem) {
                t++;
                rem--;
            }
            auto prev = cur;
            while (t--) {
                prev = cur;
                cur = cur -> next;
            }
            prev -> next = NULL;
            res.push_back(temp);
        }

        while (res.size() < k) {
            res.push_back(NULL);
        }

        return res;
    }
};