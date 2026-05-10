class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left

    def next(self, key):
        if key < self.key:
            return self.left
        elif key > self.key:
            return self.right
        else:
            return self

    def add(self, node):
        if key < self.key:
            self.left = node
        else:
            self.right = node

class MyHashMap:

    def _hash_key(self, key):
        return key % 10000

    def __init__(self):
        self.storage = [Node() for _ in range(0, 10000)]
        

    def put(self, key: int, value: int) -> None:
        """add new element to the hashmap or update the value of the element with existing key"""
        cur = self.storage[self._hash_key(key)]

        if cur.key is None:
            print(f"added root with key {key} and value {value}")
            cur.key = key
            cur.value = value
            return

        parent = None
        while cur is not None:
            if cur.key == key:
                print(f"updated value for key {key} from {cur.value} to {value}")
                cur.value = value
                return

            parent = cur
            cur = cur.left if key < cur.key else cur.right

        new_node = Node(key, value)
        print(f"adding new non-root element with key {key} and value {value}")
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        return


    def get(self, key: int) -> int:
        cur = self.storage[self._hash_key(key)]

        if cur.key is None:
            return -1 # empty collision tree

        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.left if key < cur.key else cur.right

        return -1
        
    def _remove_leaf(self, node, parent) -> Node:
        print(f"removing a leaf (parent {parent}, node {node})")
        if node.key < parent.key:
            parent.left = None
        else:
            parent.right = None

        return parent

    def _remove_node_single(self, node, parent) -> Node:
        print(f"removing target with a single child")
        # find new value to link
        new_node = node.left if node.left else node.right
        if node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        return parent


    def remove(self, key: int) -> None:
        
        parent, cur = None, self.storage[self._hash_key(key)]

        if cur.key is None:
            print(f"nothing to delete, exiting")
            return

        if cur.left is None and cur.right is None and cur.key == key:
            cur.key, cur.value = None, None
            print(f"deleted root element")
            return

        while cur is not None:
            if cur.key == key:
                # check if leaf
                if cur.left is None and cur.right is None:
                    self._remove_leaf(cur, parent)
                elif (cur.left is None and cur.right is not None) or (cur.left is not None and cur.right is None):
                    pass # delete node with single child
                else:
                    pass # remove node with two childeren

            parent = cur
            cur = cur.left if key < cur.key else cur.right
        
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)