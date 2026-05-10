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
        key_node = LinkedNode(key)
        key_hash = self.__keyhash(key)

        head_node = self.storage[key_hash]
        while head_node.nextn:
            if head_node.nextn.value == key:
                print(f"duplicate key {key} exists, aborting add operation")
                return
            head_node = head_node.nextn
        head_node.nextn = LinkedNode(key)

        #self.storage[key_hash].append(key_node)
        print(f"added node {key} with hash {key_hash}")


    def remove(self, key: int) -> None:
        key_hash = self.__keyhash(key)

        head_node = self.storage[key_hash]
        if not head_node.nextn:   # no elements in list
            print(f"cannot remove key {key} from an empty list")
            return

        while head_node.nextn.value != key:
            head_node = head_node.nextn
        print(f"removing key {key} from hash {key_hash} by rerouting {head_node.value} to {head_node.nextn.value}")
        head_node.nextn = head_node.nextn.nextn
        


    def contains(self, key: int) -> bool:
        key_hash = self.__keyhash(key)
        head_node = self.storage[key_hash]

        if not head_node.nextn:
            print(f"key {key} not found, empty list")
            return False

        head_node = head_node.nextn
        while head_node:
            if head_node.value == key:
                print(f"key {key} found under hash {key_hash}")
                return True
            head_node = head_node.nextn
        
        print(f"key {key} not found under hash {key_hash}")
        return False