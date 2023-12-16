

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bucket_array = [None for _ in range(capacity)]
        self.p = 31
        self.num_entries = 0

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
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
        return hash_code % num_buckets

    def size(self):
        return self.num_entries

    def check_capacity(self):
        return self.size() < self.capacity 
    
    def get_bucket(self):
        bucket = []
        for node in self.bucket_array:
            if node is not None:
                bucket.append(node.value)
            else:
                bucket.append(None)
        
        return bucket



class LRU_Cache(HashMap):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.previous = self.head
            self.head = node
        
        return None

    def remove_lru(self):
        new_tail = self.tail.next
        new_tail.previous = None
        self.tail.next = None
        self.tail = new_tail
        
        return None
    
    def put(self, key, value):
        node = Node(value)

        if not self.check_capacity():
            self.remove_lru()
        
        bucket_index = self.get_bucket_index(key)
        self.append(node)
        self.bucket_array[bucket_index] = node
        self.num_entries += 1

    def get(self, key):
        # Get node from bucket array
        bucket_index = self.get_hash_code(key)
        node = self.bucket_array[bucket_index]
        if node is None:
            return -1
        self.bucket_array[bucket_index] = None

        # Remove node from cache
        self.remove(node)

        # Put the node on the front
        self.append(node)
        
        return node.value
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.previous
            
    def __repr__(self):
        return str([v for v in self])
