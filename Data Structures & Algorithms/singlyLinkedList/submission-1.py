import copy 

class LinkedList:
    
    def __init__(self):

        self.value=None
        self.next=None

    
    def get(self, index: int) -> int:
        if index < 0 or self.value is None:
            return -1

        current = self

        for _ in range(index):
            if current.next is None:
                return -1
            current = current.next

        return current.value
        
        

    def insertHead(self, val: int) -> None:

         # Empty list
        if self.value is None:
            self.value = val
            return

        # Store the current head in a new LinkedList object
        old_head = LinkedList()
        old_head.value = self.value
        old_head.next = self.next

        self.value = val
        self.next = old_head

    def insertTail(self, val: int) -> None:
        new_list = LinkedList()
        new_list.value = val

        self.next = new_list
        

    def remove(self, index: int) -> bool:
        
        copy_list = copy.copy(self)
        if index !=0:
            for i in range(0,index):
                if copy_list.next !=None:
                    copy_list.next = copy_list.next.next
                else: return false
            for i in range(0,index-1):
                self.next = self.next.next
            self.next.value = self.next.next.value
            self.next = self.next.next
            return True


    def getValues(self) -> List[int]:
        output = []
        current = self

        while current is not None:
            output.append(current.value)
            current = current.next

        return output