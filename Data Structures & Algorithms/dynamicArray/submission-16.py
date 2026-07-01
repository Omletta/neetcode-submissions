class DynamicArray:

    
    def __init__(self, capacity: int):
        if capacity !=0:
            self.capacity = capacity
            self.array = [None]*capacity

    def get(self, i: int) -> int:
        
    
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
    
        if len(self.array) >= self.capacity:
            self.resize()
        if (n in self.array):
            self.array.remove(n)
        self.array[capacity]=n

        
        



    def popback(self) -> int:

        last_value = self.array.pop(self.capacity-1)
        return last_value
 

    def resize(self) -> None:

        self.capacity = self.capacity *2


    def getSize(self) -> int:
        counter = 0
        for i in range(0,len(self.array)):
            if self.array[i] != None:
                counter +=1 

        return counter 

    
        
    
    def getCapacity(self) -> int:
        return self.capacity