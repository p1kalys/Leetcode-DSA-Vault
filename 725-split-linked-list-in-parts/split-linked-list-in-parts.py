# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, cur = 0, head
        res = []

        while cur:
            cur = cur.next
            length += 1
        
        base = length // k
        rem = length % k

        cur = head

        for i in range(k):
            res.append(cur)
            for j in range(base - 1 + (1 if rem else 0)):
                if not cur: break
                cur = cur.next
            rem -= (1 if rem else 0)
            if cur:
                cur.next, cur = None, cur.next                
            
        return res