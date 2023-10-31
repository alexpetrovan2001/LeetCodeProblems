# Good solution, beats 74% time and 52% memory

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.nodes:
                node.nodes[letter] = TrieNode()
            node = node.nodes[letter]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.nodes:
                return False
            node = node.nodes[letter]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.nodes:
                return False
            node = node.nodes[letter]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("appl"))
print(obj.startsWith("apple"))
# param_3 = obj.startsWith(prefix)