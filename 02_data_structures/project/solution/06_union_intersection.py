import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
    

class LinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, value):

        node = Node(value)
        
        if self.head is None:
            self.head = node
            return
            
        node.next = self.head
        self.head = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def from_list(self, values):
        self.head = Node(values[0])

        previous_node = self.head
        for value in values[1:]:
            node = Node(value)
            previous_node.next = node
            previous_node = node
            
        return
    
    def to_list(self):
        values = []
        node = self.head
        while node:
            values.append(node.value)
            node = node.next
        return values
    
    def __str__(self):
        values = self.to_list()
        out_string = "["
        for value in sorted(values):
            out_string += str(value) + " "
        out_string = out_string[:-1]
        out_string += "]"
        return out_string


class ChainNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    
    def __init__(self, initial_size=15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = ChainNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient
        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)         # we can use our put() method to rehash
                head = head.next
                
    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

    
    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output
    


def union(llist_1, llist_2):
    
    if llist_1 is None or llist_2 is None:
        return

    llist_union = LinkedList()
    hash_map = HashMap()

    # Iterate first linked list
    node = llist_1.head
    while node is not None:
        
        value = node.value
        if hash_map.get(value) is None:
            hash_map.put(value, value)
            llist_union.append(value)

        node = node.next

    node = llist_2.head
    while node is not None:
        
        value = node.value
        if hash_map.get(value) is None:
            hash_map.put(value, value)
            llist_union.append(value)

        node = node.next

    return llist_union


def intersection(llist_1, llist_2):

    if llist_1 is None or llist_2 is None:
        return
    
    llist = LinkedList()
    hash_map = HashMap()

    # Iterate first linked list
    node = llist_1.head
    while node is not None:
        
        value = node.value
        count = hash_map.get(value)
        if count is None:
            hash_map.put(value, 1)
            
        node = node.next

    # Iterate second linked list
    node = llist_2.head
    while node is not None:  
        
        value = node.value
        count = hash_map.get(value)
        
        if count == 1:
            hash_map.put(value, 2)
            llist.append(value)            
            
        node = node.next

    return llist


def test_union():
    list_1 = np.array([2, 3, 3, 4, 4, 6, 6, 21, 35, 65])
    list_2 = np.array([1, 1, 4, 6, 6, 9, 11, 21, 32])

    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.from_list(list_1.tolist())
    llist_2.from_list(list_2.tolist())

    llist = union(llist_1, llist_2)

    assert set(np.union1d(list_1, list_2).tolist()) == set(llist.to_list())


def test_intersection():
    list_1 = np.array([2, 3, 3, 4, 4, 6, 6, 21, 35, 65])
    list_2 = np.array([1, 1, 4, 6, 6, 9, 11, 21, 32])

    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.from_list(list_1.tolist())
    llist_2.from_list(list_2.tolist())

    llist = intersection(llist_1, llist_2)

    assert set(np.intersect1d(list_1, list_2).tolist()) == set(llist.to_list())


def test_null():
    list_1 = np.array([2, 3, 3, 4, 4, 6, 6, 21, 35, 65])
    llist_1 = LinkedList()
    llist_1.from_list(list_1.tolist())

    llist_2 = None

    assert union(llist_1, llist_2) is None
    assert intersection(llist_1, llist_2) is None



if __name__ == "__main__":
    test_intersection()
    test_union()
    test_null()