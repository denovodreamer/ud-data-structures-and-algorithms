

import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = ""
        hash_str += str(self.timestamp)
        hash_str += str(self.data)
        hash_str += str(self.previous_hash)

        sha.update(hash_str.encode('utf-8'))

        return sha.hexdigest()
    


class BlockChain:

    def __init__(self):
        self.tail = None

    def add_block(self, data):
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if self.tail is None:
            previous_hash = "0"
            self.tail = Block(timestamp, data, previous_hash)
            return

        last_block = self.tail
        previous_hash = last_block.hash
        
        new_block = Block(timestamp, data, previous_hash)
        new_block.previous = last_block
        
        self.tail = new_block


if __name__ == "__main__":

    block_chain = BlockChain()

    for i in range(3):
        block_chain.add_block(f"Data from block {i}!")

    block_chain.tail.data