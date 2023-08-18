class RandomizedCollection:

    def __init__(self):
        self.stack = []
        

    def insert(self, val: int) -> bool:
        
        if val not in self.stack:
            self.stack.append(val)
            return True  
        else:      
            self.stack.append(val)
            return False
        
        

    def remove(self, val: int) -> bool:
        if val in self.stack:
            self.stack.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()