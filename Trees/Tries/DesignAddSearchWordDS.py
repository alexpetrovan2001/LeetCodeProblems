# Good solution, beats 73% time and 45% memory

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.nodes:
                node.nodes[letter] = TrieNode()
            node = node.nodes[letter]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(pattern, node):
            if not pattern:
                return node.is_word
            letter = pattern[0]
            if letter != "." and letter in node.nodes:
                res = dfs(pattern[1:], node.nodes[letter])
                if res:
                    return True
            elif letter == ".":
                for tree_letter in node.nodes:
                    if dfs(pattern[1:], node.nodes[tree_letter]):
                        return True
            else:
                return False

        node = self.root
        res = dfs(word, node)
        return True if res else False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
print(
wordDictionary.addWord("at"),
wordDictionary.addWord("and"),
wordDictionary.addWord("an"),
wordDictionary.addWord("add"),
wordDictionary.search("a"),
wordDictionary.search(".at"),
wordDictionary.addWord("bat"),
wordDictionary.search(".at"),
wordDictionary.search("an."),
wordDictionary.search("a.d."),
wordDictionary.search("b."),
wordDictionary.search("a.d"),
wordDictionary.search(".")
)