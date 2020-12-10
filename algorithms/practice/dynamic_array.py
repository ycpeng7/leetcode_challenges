#-------------------------------------------------------------------------------
#    Implementation of dynamic array
#-------------------------------------------------------------------------------

class DynamicArray:
    def __init__(self, capacity: int=0):
        if capacity < 0:
            raise "Illegal Capacity"
        self.d_array = [None] * capacity
        self.capacity = capacity
        self.length = 0
    
    def size(self) -> int:
        return self.length
    
    def isEmpty(self) -> bool:
        return self.length == 0
    
    def get(self, index: int):
        return self.d_array[index]

    def clear(self):
        for i in range(self.capacity):
            self.d_array[i] = None
        self.length = 0
    
    def add(self, element):
        if self.length == self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.length):
                new_arr[i] = self.d_array[i]
            self.d_array = new_arr
        self.d_array[self.length] = element
        self.length += 1

    def remove_by_index(self, index: int):
        if index >= self.length:
            raise "Index out of bound"
        for i in range(index, self.length):
            self.d_array[i] = self.d_array[i + 1]
        self.length -= 1

    def remove_by_element(self, element):
        for index, value in enumerate(self.d_array):
            if value == element:
                self.remove_by_index(index)
    
    

