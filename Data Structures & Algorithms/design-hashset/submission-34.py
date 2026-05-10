class LinkedNode:
    """Linked list node"""
    def __init__(self, key):
        self.value = key
        self.nextn = None

class MyHashSet:

    # INIT_CAPACITY = 10000

    def __keyhash(self, key):
        return key % 10000

    def __init__(self):
        self.storage = [LinkedNode(0) for _ in range(10000)]

    def add(self, key: init) -> None:
        """Add new key by iterating through appropriate colision list and checking if the key already exists. The implementation uses 
        two pointers - head na previous pointer tracking the head."""
        key_node = LinkedNode(key)
        key_hash = self.__keyhash(key)

        head_node, prev_node = self.storage[key_hash], None
        while head_node:               # iterate until last key (exists loop on the last key without value check)
            if head_node.value == key: # there is already the same key in the list, just exit
                return
            prev_node, head_node = head_node, head_node.nextn

        prev_node.nextn = LinkedNode(key)    # add new key at the end of the list

    def remove(self, key: int) -> None:
        """
        Remove from the arbitrary position in the list.
        Always located on the previous key comparing to the key that is being checked. 
        That support deleting from the beggining, middle and the end.
        """
        key_hash = self.__keyhash(key)
        head_node = self.storage[key_hash]

        if not head_node.nextn:         # no set keys in list, just dummy key - exit
            return

        while head_node.nextn.value != key:
            head_node = head_node.nextn
        head_node.nextn = head_node.nextn.nextn

    def contains(self, key: int) -> bool:
        key_hash = self.__keyhash(key)
        head_node = self.storage[key_hash]

        if not head_node.nextn:         # no keys in this key list
            return False

        head_node = head_node.nextn     # start from the first non-dummy key
        while head_node:
            if head_node.value == key:
                return True
            head_node = head_node.nextn
        
        return False