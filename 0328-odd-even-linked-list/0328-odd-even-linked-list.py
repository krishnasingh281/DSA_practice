# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        list1 = []
        current = head
        
        while current is not None:
            list1.append(current.val)
            current = current.next

        current = head

        for i in range(0, len(list1), 2):
            current.val = list1[i]
            current = current.next

        for i in range(1, len(list1), 2):
            current.val = list1[i]
            current = current.next
            
        return head