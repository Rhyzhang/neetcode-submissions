# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        if head.next == None:
            return head

        start_head = head
        i = 0

        while start_head.next != None:
            head_temp = start_head
    
            while head_temp.next != None:
                prev = head_temp
                head_temp = head_temp.next

            head_temp.next = prev
            prev.next = None

            if i == 0:
                head_final = head_temp
            
            i+= 1
        
        return head_final

        # new_head = ListNode(head.val, head.next)

        

        
