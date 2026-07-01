class DynamicArray:

    
    def __init__(self, capacity: int):
        if capacity !=0:
            self.capacity = capacity
            self.array = [none]*capacity

    def get(self, i: int) -> int:
        
        if i <= (capacity - 1):
            element_of_index = self.array[i]
    
        return element_of_index


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        
        if (len[self.array]>=self.capacity):
            self.resize()
            self.array.remove(n)
            self.array.append(n)

        self.array.remove(n)
        self.array.append(n)



    def popback(self) -> int:

        last_value = self.array.pop(capacity-1)
        return last_value
 

    def resize(self) -> None:

        self.capacity = self.capacity *2


    def getSize(self) -> int:
        return len(self.array)
        
    
    def getCapacity(self) -> int:
        return self.capacity