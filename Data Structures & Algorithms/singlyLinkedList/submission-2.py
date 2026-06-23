from typing import List


class LinkedList:
    def __init__(self):
        self.value = None
        self.next = None

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
        # Empty list
        if self.value is None:
            self.value = val
            return

        current = self

        while current.next is not None:
            current = current.next

        new_item = LinkedList()
        new_item.value = val
        current.next = new_item

    def remove(self, index: int) -> bool:
        if index < 0 or self.value is None:
            return False

        # Remove the head
        if index == 0:
            if self.next is None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next

            return True

        previous = self

        for _ in range(index - 1):
            if previous.next is None:
                return False
            previous = previous.next

        if previous.next is None:
            return False

        previous.next = previous.next.next
        return True

    def getValues(self) -> List[int]:
        if self.value is None:
            return []

        output = []
        current = self

        while current is not None:
            output.append(current.value)
            current = current.next

        return output