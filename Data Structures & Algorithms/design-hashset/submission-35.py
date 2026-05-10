### SOLUTION 3 - Optimal time&space complexity using linked list
class LinkedNode:
    """Linked list node"""
    def __init__(self, key):
        self.value = key
        self.nextn = None

class MyHashSet:
    # time complexity notes
    # b - number of buckets
    # N - number of keys
    # L - collision chain length, 0 <= L <= N, avg. case L = N/m if hashes are well separated

    def __keyhash(self, key):
        return key % 10000

    def __init__(self):
        # time complexity O(b)
        # space complexity O(b)
        self.storage = [LinkedNode(None) for _ in range(10000)]

    def add(self, key: init) -> None:
        """Add new key by iterating through appropriate colision list and checking if the key already exists. 
        Uses two pointer implementation - one pointer for prev and one for curent element."""
        # time complexity: O(1) to access bucket, O(L) to traverse through collision list (O(N) worst, O(N/m) avg.), O(1) to add new element
        # total: O(L)
        # space complexity O(1) - fixed additional space for every addition
        key_hash = self.__keyhash(key)

        prev = self.storage[key_hash]
        cur = prev.nextn
        while cur:
            if cur.value == key:
                return
            prev, cur = cur, cur.nextn

        prev.nextn = LinkedNode(key)

    def remove(self, key: int) -> None:
        """
        Remove from the arbitrary position in the list. 
        Uses two pointer implementation - one pointer for prev and one for curent element.
        """
        # time complexity O(L), similar reasoning as for add operation
        # space complexity: O(1)
        key_hash = self.__keyhash(key)
        prev = self.storage[key_hash]
        cur = prev.nextn

        while cur:
            if cur.value == key:
                prev.nextn = cur.nextn
                return
            prev, cur = cur, cur.nextn

    def contains(self, key: int) -> bool:
        # time complexity O(L) - similar reasoning as for remove and add operations
        # space complexity O(1)
        """Check if there is a key in a set. Skips dummy entry and uses single pointer implementation."""
        key_hash = self.__keyhash(key)
        cur = self.storage[key_hash].nextn

        while cur:
            if cur.value == key:
                return True
            cur = cur.nextn

        return False