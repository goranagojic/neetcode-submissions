class LinkedNode:
    """Linked list node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextn = None

class MyHashMap:

    def __keyhash(self, key):
        return key % 10000

    def __init__(self):
        self.storage = [LinkedNode(None, None) for _ in range(10000)]
        

    def put(self, key: int, value: int) -> None:
        """Inserts a new key, value pair into the hashmap. If key already exists in the map, update the corresponding value."""
        # time complexity: O(1) to access bucket, O(L) to traverse through collision list (O(N) worst, O(N/m) avg.), O(1) to add new element
        # total: O(L)
        # space complexity O(1) - fixed additional space for every addition
        key_hash = self.__keyhash(key)

        prev = self.storage[key_hash]
        cur = prev.nextn
        while cur:
            if cur.key == key:
                cur.value = value
                return
            prev, cur = cur, cur.nextn

        prev.nextn = LinkedNode(key, value)

    def get(self, key: int) -> int:
        # time complexity O(L) - similar reasoning as for remove and add operations
        # space complexity O(1)
        """Returns the value to which the specified key is mapped or -1 if this map contains no mapping for the key."""
        key_hash = self.__keyhash(key)
        cur = self.storage[key_hash].nextn

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.nextn

        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the key and its corresponding value if the map contains the mapping for the key.
        """
        # time complexity O(L), similar reasoning as for add operation
        # space complexity: O(1)
        key_hash = self.__keyhash(key)
        prev = self.storage[key_hash]
        cur = prev.nextn

        while cur:
            if cur.key == key:
                prev.nextn = cur.nextn
                return
            prev, cur = cur, cur.nextn

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)