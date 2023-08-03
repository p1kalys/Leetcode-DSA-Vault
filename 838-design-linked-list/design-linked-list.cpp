class MyLinkedList {
public:
ListNode*  head;
    MyLinkedList() {
        head=new ListNode(0);
        head->next=nullptr;       
    }
    
    int get(int index) {
        return getCount(head,index,-1);
    }
    int getCount(ListNode* cur,int index, int count){
        if(cur==nullptr)return -1;
        if(index==count) return cur->val;
        return getCount(cur->next,index,count+1);
    }
    void addAtHead(int val) {
        ListNode* h=new ListNode(val);
        h->next=head->next;
        head->next=h;
        return;
    }
    
    void addAtTail(int val) {
        ListNode* t=head;
        while(t!=nullptr && t->next!=nullptr) {
            t=t->next;
        }
        t->next=new ListNode(val);
        return;
    }
    
    void addAtIndex(int index, int val) {
        int count=0;
        ListNode* h=head;
        while(h->next!=nullptr && count<index){
            h=h->next;
            count++;
        }
        if (count==index){
            if(h->next==nullptr){
                h->next=new ListNode(val);
            }
            else{
                ListNode* p=h->next;
                h->next=new ListNode(val);
                h->next->next=p;
            }
        }
        return;
    }
    
    void deleteAtIndex(int index) {
        int count = 0;
        ListNode* n = head;
        while(n->next != nullptr && count < index){
            n = n->next;
            count++;
        }
        if(count == index){
            if(n->next == nullptr)
                return;
            else{
                ListNode* p = n->next->next;
                delete n->next;
                n->next = p;
            }
        }
        return;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */