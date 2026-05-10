class MyHashSet:
    # space complexity is O(1) - O(1000000)
    # time complexity O(n) for set creation, O(1) for adding, removal and contains operation

    MAX_CAPACITY = 1000000

    def __init__(self):
        self.storage = [False] * self.MAX_CAPACITY
        

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