"Time Complexity is O(N*L)"
"Space Complexity is O(N*L)"

#Explanation
"A Trie stores words by splitting them into characters and creating tree-like nodes."
"Insertions involve character-by-character traversal, adding nodes where needed."
"Search checks if a word exists by traversing nodes, ending at endofword."
"Prefix Checks traverse only as far as the given prefix, verifying existence."

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endofword = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def _get_index(self, char: str) -> int:
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = self._get_index(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.endofword = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = self._get_index(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.endofword

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = self._get_index(char)
            if not node.children[index]:
                return False
            node = node.children[index]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)