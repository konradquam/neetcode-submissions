class DynamicArray:
    array = []
    curr_size = -1
    capacity = 0
    
    def __init__(self, capacity: int):
        self.array = [0 for _ in range(capacity)]
        self.capacity = capacity
        print(capacity, self.capacity)
        return


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        return


    def pushback(self, n: int) -> None:
        self.curr_size += 1
        if self.curr_size == self.capacity:
            self.resize()
        self.array[self.curr_size] = n
        return


    def popback(self) -> int:
        item = self.array[self.curr_size]
        self.curr_size -= 1
        return item
 

    def resize(self) -> None:
        new_array = [0 for _ in range(2*self.capacity)]
        for i in range(self.curr_size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity *= 2
        return

    def getSize(self) -> int:
        return self.curr_size + 1
    
    def getCapacity(self) -> int:
        return self.capacity
