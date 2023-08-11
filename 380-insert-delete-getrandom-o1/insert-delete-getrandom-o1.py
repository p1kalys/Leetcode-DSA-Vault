class RandomizedSet(object):

    def __init__(self):
        self.nums = [] #a list store values
        self.valToIndex = {} #dictionary maps to indices in self.nums
      
    # not exists-> insert -> return True
    # exists -> return False
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.nums) #add val to dict
        self.nums.append(val) # add val to self.nums
        return True

        
    # exists -> remove ->return True
    # remove: swap with the last -> pop
    # not exists -> return False
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.valToIndex:
            return False
        index = self.valToIndex[val] # get val's index
        self.valToIndex[self.nums[-1]] = index # change the last val to current index
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index] # swaps the positions of the value
        self.nums.pop()
        del self.valToIndex[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()