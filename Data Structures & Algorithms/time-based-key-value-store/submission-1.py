class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map : 
            self.map[key] = {}
            self.map[key][timestamp] = value 
        else:
            self.map[key][timestamp] = value

        

    def get(self, key: str, timestamp: int) -> str:
        best_timestamp = -1
        if key not in self.map :
            return ''

        for t in self.map[key] :
            if t<= timestamp and t > best_timestamp : 
                best_timestamp = t 
            
        if best_timestamp == -1 :
            return ''

        

        return self.map[key][best_timestamp]


        
        
