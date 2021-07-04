import hashlib as hasher
from datetime import datetime


class Block(object):
    """docstring for Block"""

    def __init__(self, index, timestramp, data, previous_hash):
        super(object, self).__init__()
        self.index = index
        self.timestramp = timestramp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return 'Block #{}'.format(self.index)

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (self.index, self.timestramp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()

    def make_genesis_block(self):
        block = Block(index=0, timestramp=datetime.now(), data='Genesis Block', previous_hash='0')
        return block

    def next_block(last_block, data=''):
        """ Return next block in a block-chain."""
        idx = last_block.index + 1
        block = Block(index=idx, timestramp=datetime.now, data='{}{}'.format(data, idx), previous_hash=last_block.hash)
        return block


def test_code():
    """ Test creating chain of 20 blocks."""
    blockchain = [Block.make_genesis_block()]
    prev_block = blockchain[0]

    for _ in range(0, 20):
        block = Block.next_block(prev_block, data='some data here')
        blockchain.append(block)
        prev_block = block
        print('{} added to blockchain'.format(block))
        print('Hash:{}\n'.format(block.hash))


# run the text code
# if __name__ == '__main__':
test_code()
