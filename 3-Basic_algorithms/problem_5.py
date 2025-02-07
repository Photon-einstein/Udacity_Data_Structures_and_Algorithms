## Represents a single node in the Trie
class TrieNode:
    def __init__(self) -> None:
        ## Initialize this node in the Trie
        self.SIZE_ALPHABET = 26
        self.child = [None] * self.SIZE_ALPHABET
        self.wordEnd = False

    def insert(self, char: str) -> None:
        ## Add a child node in this Trie
        if len(char) == 0:
            return
        char = char.lower()
        index = ord(char[0]) - ord("a")
        # insertion if node still not there
        if self.child[index] == None:
            self.child[index] = TrieNode()
        # Test end of word
        if len(char) == 1:
            self.child[index].wordEnd = True
        else:
            self.child[index].insert(char[1:])

    def suffixes(self, suffix: str = "") -> list[str]:
        """Recursive function that collects the suffix for
        all complete words below this point"""
        words = list()

        if self.wordEnd and suffix:
            words.append(suffix)

        for i in range(self.SIZE_ALPHABET):
            if self.child[i] is not None:
                next_char = chr(ord("a") + i)
                words.extend(self.child[i].suffixes(suffix + next_char))

        return words


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self) -> None:
        """Initialize this Trie (add a root node)"""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Add a word to the Trie"""
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current.child[index] is None:
                current.child[index] = TrieNode()
            current = current.child[index]
        current.wordEnd = True

    def find(self, prefix: str) -> TrieNode | None:
        """Find the Trie node that represents this prefix"""
        if len(prefix) == 0:
            return None
        node_search = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if node_search.child[index] is None:
                return None
            node_search = node_search.child[index]
        return node_search


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix: str) -> None:
    if prefix != "":
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print("\n".join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print("")


# Edge case: Empty string
prefixNode = MyTrie.find("")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
assert prefixNode == None
print("\nTest 1: input empty string pass\n")
# Expected output: False

# Normal case: Word present in the Trie
prefixNode = MyTrie.find("ant")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
suffixes_list = prefixNode.suffixes()
assert len(suffixes_list) == 3
assert "agonist" in suffixes_list
assert "hology" in suffixes_list
assert "onym" in suffixes_list
print("\nTest 2: 'ant' input pass\n")
# Expected output: True

# Test case: Word present in the Trie, no suffixes
prefixNode = MyTrie.find("function")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
suffixes_list = prefixNode.suffixes()
assert len(suffixes_list) == 0
print("\nTest 3: 'function' input pass\n")
# Expected output: True

# Normal case: Prefix of a word present in the Trie
prefixNode = MyTrie.find("fun")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
suffixes_list = prefixNode.suffixes()
assert len(suffixes_list) == 1
assert "ction" in suffixes_list
print("\nTest 4: 'fun' input pass\n")
# Expected output: True

# Normal case: Prefix of a word present in the Trie
prefixNode = MyTrie.find("f")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
suffixes_list = prefixNode.suffixes()
assert len(suffixes_list) == 3
assert "actory" in suffixes_list
assert "un" in suffixes_list
assert "unction" in suffixes_list
print("\nTest 5: 'f' input pass\n")
# Expected output: True

# Edge case: Prefix of a word not present in the Trie
prefixNode = MyTrie.find("z")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
assert prefixNode == None
print("\nTest 6: 'z' input pass\n")
# Expected output: True

# Normal case: Prefix of a word present in the Trie
prefixNode = MyTrie.find("tri")
print("\n".join(prefixNode.suffixes())) if prefixNode else print(prefixNode)
suffixes_list = prefixNode.suffixes()
assert len(suffixes_list) == 4
assert "e" in suffixes_list
assert "gger" in suffixes_list
assert "gonometry" in suffixes_list
assert "pod" in suffixes_list
print("\nTest 7: 'tri' input pass\n")
# Expected output: True
