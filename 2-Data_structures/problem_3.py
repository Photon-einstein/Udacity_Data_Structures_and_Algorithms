import heapq
from collections import defaultdict
from typing import Optional


# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

    def __lt__(self, other: "HuffmanNode") -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq

    def __repr__(self):
        return f"HuffmanNode({self.char} : {self.freq})"


def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    dict = {}
    for char in data:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    huffman_tree = []
    for key, value in frequency.items():
        huffman_node = HuffmanNode(key, value)
        heapq.heappush(huffman_tree, huffman_node)

    # combine nodes until there is only one node left
    while len(huffman_tree) > 1:
        left_node = heapq.heappop(huffman_tree)
        right_node = heapq.heappop(huffman_tree)
        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(huffman_tree, merged_node)

    return huffman_tree[0] if huffman_tree else None


def generate_huffman_codes(
    node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]
) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node is None:
        return
    if node.char is not None:
        huffman_codes[node.char] = code
    generate_huffman_codes(node.left, code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    if not data:
        return "", None
    frequency = calculate_frequencies(data)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = dict()
    initial_code = ""
    generate_huffman_codes(huffman_tree, initial_code, huffman_codes)
    # Special case: if there is only one unique character, then the code "0" is assigned
    if len(frequency) == 1:
        unique_char = next(iter(frequency.keys()))
        huffman_codes[unique_char] = "0"
    encoded_huffman_data = ""
    for char in data:
        encoded_huffman_data += huffman_codes[char]
    return encoded_huffman_data, huffman_tree


def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    decoded_string = ""

    # Special case: if the tree consists of a single node, decode accordingly
    if not tree.left and not tree.right:
        return tree.char * len(encoded_data)

    index = 0
    while index < len(encoded_data):
        node = tree
        while node.left or node.right:
            if encoded_data[index] == "0":
                node = node.left
            else:
                node = node.right
            index += 1

        decoded_string += node.char
    return decoded_string


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence_1 = "Huffman coding is fun!"
    encoded_data_1, tree = huffman_encoding(sentence_1)
    decoded_data_1 = huffman_decoding(encoded_data_1, tree)
    assert sentence_1 == decoded_data_1

    # Test Case 2: Empty string
    print("Test Case 2: Empty string")
    sentence_2 = ""
    encoded_data_2, tree = huffman_encoding(sentence_2)
    assert encoded_data_2 == "" and tree == None

    # Test Case 3: Special characters
    print("Test Case 3: Long string of same characters")
    sentence_3 = "A" * 100
    encoded_data_3, tree = huffman_encoding(sentence_3)
    decoded_data_3 = huffman_decoding(encoded_data_3, tree)
    assert sentence_3 == decoded_data_3
