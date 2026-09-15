# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        count  = 0
        current = head
        
        tracker = None

        while current :
            current = current.next
            prev = current 
            count +=1

        if count == 1 :
            return None

        for i in range(0, count - n) :
            tracker = head.next
            
        if tracker != None and tracker.next !=None :
            tracker.next = tracker.next.next
        print(head)
        return head


        