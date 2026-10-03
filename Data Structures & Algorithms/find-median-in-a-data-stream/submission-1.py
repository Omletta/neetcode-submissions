class MedianFinder:

    def __init__(self):
        self.nums = []
        self.length = 0
    def addNum(self, num: int) -> None:

        self.nums.append(num)
        self.length +=1
        

    def findMedian(self) -> float:
        self.nums.sort()

        if self.length %2 !=0:
            mid = self.length //2 
            return self.nums[mid]
        else:
            mid = (self.length-1) //2 

            return (self.nums[mid] + self.nums[mid+1])/2


        
            
        