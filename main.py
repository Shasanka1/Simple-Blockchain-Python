import hashlib # for hashing

import unittest # for testing
import typing # for type checking

# This is the main function


class Blockchain: # block class

    def __init__(self, previous_block_hash: str , transaction_list : list): # constructor
        self.previous_block_hash = previous_block_hash # previous block hash
        self.transaction_list = transaction_list # list of transactions
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash # data to be hashed
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # hash of the block


# create genesis block
'''
Genesis block is the first block in the blockchain. It is the block that starts the chain.

The structure is like a reverse LinkedList structure where the genesis block is the head of the chain.
'''

# Unit Testing
# This is the unit testing for the blockchain class
'''
The unit testing is done using the unittest module.

'''

class TestStringMethods(unittest.TestCase ): # test class
    
        def test_blockchain(self):
            t1 = " Anna sent 2 BTC to Bob "
            t2 = " Bob sent 1 BTC to Charlie "
            t3 = " Charlie sent 0.5 BTC to Anna "
            t4 = " Anna sent 0.5 BTC to Bob "
            t5 = " Bob sent 0.5 BTC to Charlie "
            t6 = " Charlie sent 0.5 BTC to Anna "
    
            inital_block = Blockchain("Initial String", [t1, t2])
            second_block = Blockchain(inital_block.block_hash, [t3, t4])
            third_block = Blockchain(second_block.block_hash, [t5, t6])
    
            self.assertEqual(inital_block.block_hash, "d0b0c3c7f8a3a3d9a2b2e4a4a4c4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4")
            self.assertEqual(second_block.block_hash, "d0b0c3c7f8a3a3d9a2b2e4a4a4c4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4")
            self.assertEqual(third_block.block_hash, "d0b0c3c7f8a3a3d9a2b2e4a4a4c4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4f4")
        
if __name__ == '__main__':
    unittest.main() # run the unit test
    
