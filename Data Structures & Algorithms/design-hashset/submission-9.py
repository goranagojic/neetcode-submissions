class MyHashSet:

    CAPACITY = 1000000

    def __init__(self):
        self.storage = [False] * self.CAPACITY
        

    def add(self, key: int) -> None:
        self.storage[key] = True
        

    def remove(self, key: int) -> None:
        self.storage[key] = False

    def contains(self, key: int) -> bool:
        return self.storage[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)