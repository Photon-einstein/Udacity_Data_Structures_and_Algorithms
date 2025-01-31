import hashlib
import datetime
from llist import sllist, sllistnode


class Block:
    """
    A class to represent a block in the blockchain.

    Attributes:
    -----------
    timestamp : datetime.datetime
        The timestamp when the block was created.
    data : str
        The data stored in the block.
    previous_hash : str
        The hash of the previous block in the chain.
    hash : str
        The hash of the current block.
    """

    def __init__(
        self, timestamp: datetime.datetime, data: str, previous_hash: str
    ) -> None:
        """
        Constructs all the necessary attributes for the Block object.

        Parameters:
        -----------
        timestamp : datetime.datetime
            The timestamp when the block was created.
        data : str
            The data stored in the block.
        previous_hash : str
            The hash of the previous block in the chain.
        """
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.

        Returns:
        --------
        str
            The hash of the block.
        """
        sha = hashlib.sha256()
        hash_str = (
            str(self.timestamp) + str(self.data) + str(self.previous_hash)
        ).encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """
        Return a string representation of the block.

        Returns:
        --------
        str
            A string representation of the block.
        """
        return (
            f"Block(\n"
            f"  Timestamp: {self.timestamp},\n"
            f"  Data: {self.data},\n"
            f"  Previous Hash: {self.previous_hash},\n"
            f"  Hash: {self.hash}\n"
            f")\n"
        )


class Blockchain:
    """
    A class to represent a blockchain.

    Attributes:
    -----------
    chain : list[Block]
        The list of blocks in the blockchain.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Blockchain object.
        """
        self.blockchain = sllist()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (the first block in the blockchain).
        """
        # Genesis block has no previous hash and empty data
        timestamp = datetime.datetime.now()
        data = ""
        previous_hash = ""
        genesis_block = Block(timestamp, data, previous_hash)
        self.blockchain.append(genesis_block)

    def add_block(self, data: str) -> None:
        """
        Add a new block to the blockchain.

        Parameters:
        -----------
        data : str
            The data to be stored in the new block.
        """
        timestamp = datetime.datetime.now()
        previous_hash = self.blockchain.last().hash
        genesis_block = Block(timestamp, data, previous_hash)
        self.blockchain.append(genesis_block)

    def __repr__(self) -> str:
        """
        Return a string representation of the blockchain.

        Returns:
        --------
        str
            A string representation of the blockchain.
        """
        chain_str = ""
        for block in self.blockchain:
            chain_str += str(block) + "\n"
        return chain_str


if __name__ == "__main__":
    # Test cases
    # Test Case 1: Create a blockchain and add blocks
    print("Test Case 1: Basic blockchain functionality")
    blockchain_1 = Blockchain()
    # Test genesis block creation
    assert len(blockchain_1.blockchain) == 1
    genesis_block = blockchain_1.blockchain.first()
    assert genesis_block.data == ""
    assert genesis_block.previous_hash == ""

    # Test Case 2: Block addition
    print("Test Case 2: Block addition")
    blockchain_2 = Blockchain()
    genesis_block_2 = blockchain_2.blockchain.first()
    blockchain_2.add_block("Block 1 Data")
    block_1 = blockchain_2.blockchain.last()
    assert len(blockchain_2.blockchain) == 2
    assert block_1.previous_hash == genesis_block_2.hash
    assert block_1.data == "Block 1 Data"

    # Test Case 3: Multiple blocks addition
    print("Test Case 3: Multiple blocks addition")
    blockchain_3 = Blockchain()
    blockchain_3.add_block("Block 1 Data")
    block_1 = blockchain_3.blockchain.last()
    blockchain_3.add_block("Block 2 Data")
    block_2 = blockchain_3.blockchain.last()
    assert block_1.hash == block_2.previous_hash
    blockchain_3.add_block("Block 3 Data")
    block_3 = blockchain_3.blockchain.last()
    assert len(blockchain_3.blockchain) == 4
    assert block_2.data == "Block 2 Data"
    assert block_3.data == "Block 3 Data"

    # Test Case 4: Test hash calculation
    print("Test Case 4: Hash calculation\n")
    blockchain_4 = Blockchain()
    blockchain_4.add_block("Block 1 Data")
    blockchain_4.add_block("Block 2 Data")
    blockchain_4.add_block("Block 3 Data")
    blockchain_4.add_block("Block 4 Data")
    block = blockchain_4.blockchain.last()
    expected_hash = block.calc_hash()
    assert block.hash == expected_hash

    print(f"Blockchain content: \n{blockchain_4}")

    print("Test Case 1: Basic blockchain functionality passed")
    print("Test Case 2: Block addition passed")
    print("Test Case 3: Multiple blocks addition passed")
    print("Test Case 4: Test hash calculation passed")
