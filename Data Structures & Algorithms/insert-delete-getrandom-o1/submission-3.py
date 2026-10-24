class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.size = 0
        self.arr = []

    def insert(self, val: int) -> bool:
        h = RandomizedSet()
        if val not in self.h:
            self.h[val] = self.size
            self.size +=1
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        h = RandomizedSet()
        if val in self.h:
            index = self.h[val]
            del self.h[val]
            self.size -= 1

            last = len(self.arr) -1

            if index != last:


                last = self.arr[-1] 


                self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]

                self.h[last] = index

                self.arr.pop()
            else:
                self.arr.pop()

            return True
        else:
            return False
        

    def getRandom(self) -> int:
        h = RandomizedSet()
        print(self.size)
        rando = random.choice(self.arr)
        return rando
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()