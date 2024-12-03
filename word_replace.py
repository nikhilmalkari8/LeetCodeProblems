"Time Complexity is O(N*L + M*L)"
"Space Complexity is O(N*L)"


#Explanation
"Build a Trie from the dictionary, where each word acts as a prefix (root) to match against."
"Split the sentence into words and check each word in the Trie for its shortest matching root."
"Replace the word with its root if found, or keep the original word if no root exists."
"Reconstruct the sentence with replaced words and return the result."

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endofword = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = ""
        for word in dictionary:
            self.addwords(word)
        
        listofwords = sentence.split(" ")
        
        for word in listofwords:
            shorter_version = self.get_shorter_version(word)
            result = result + shorter_version + " "
        
        return result[:-1]
    
    def get_index(self, char):
        return ord(char) - ord('a')
    
    def addwords(self, word):
        node = self.root
        for char in word:
            index = self.get_index(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.endofword = True
    
    def get_shorter_version(self,word):
        node = self.root
        string = ""
        for char in word:
            index = self.get_index(char)
            if not node.children[index]:
                return word
            node = node.children[index]
            string = string + char
            if node.endofword == True:
                return string
        return word


            
    

        