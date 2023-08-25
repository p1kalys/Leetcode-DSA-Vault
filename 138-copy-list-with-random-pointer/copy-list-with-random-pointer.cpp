/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) {
            return NULL;
        }
        
        // Step 1: Create a new node for each original node and link them together
        Node* curr = head;
        while(curr != NULL){
            Node* temp = new Node(curr -> val);
            temp -> next = curr -> next;
            curr -> next = temp;
            curr = temp -> next;
        }
        
        // Step 2: Update the random pointers in the new nodes
        curr = head;
        while(curr != NULL){
            if(curr -> random != NULL){
                curr -> next -> random = curr -> random -> next; 
            }
            curr = curr -> next -> next;
        }
        
        // Step 3: Separate the original list and the copied list
        Node* newHead = head -> next;
        Node* currOld = head;
        Node* currNew = newHead;

        while(currOld != NULL){
            currOld -> next = currNew -> next;
            currOld = currOld -> next;
            if(currOld != NULL){
                currNew -> next = currOld -> next;
                currNew = currNew -> next;
            }
        }
        return newHead;
    }
};