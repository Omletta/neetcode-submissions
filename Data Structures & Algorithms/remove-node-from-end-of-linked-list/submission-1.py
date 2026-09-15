# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []

        current = head

        while current : 
            nodes.append(current)
            current = current.next

        index_to_remove = len(nodes) - n
        if nodes[index_to_remove] == head :
            return head.next
        if nodes[index_to_remove] != None and nodes[index_to_remove].next != None :

            nodes[index_to_remove-1].next = nodes[index_to_remove].next

        return head

        


        
        