# class MyHashSet:
    # Limitations
    # - limited to int values
    # - limited to value rance [0,1M]
    # - always of the size 1M * sizeof(int), even when there is a single element in a dataset
    # Pros:
    # - O(1) for add, remove and contains operations

    # CAPACITY = 1000000

    # def __init__(self):
    #     self.storage = [False] * self.CAPACITY    

    # def add(self, key: int) -> None:
    #     self.storage[key] = True

    # def remove(self, key: int) -> None:
    #     self.storage[key] = False

    # def contains(self, key: int) -> bool:
    #     return self.storage[key]


class MyHashSet:

    def __init__(self):
        self.added, self.removed = [], []

    def add(self, key: int) -> None:
        if key not in self.added:
            self.added.append(key)
            if key in self.removed:
                self.removed.remove(key)

    def remove(self, key: int) -> None:
        if key in self.added:
            self.removed.append(key)
            print(f"removed {key}")
            self.added.remove(key)
            print(f"deleted from added {key}")

    def contains(self, key: int) -> bool:
        return key in self.added
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)