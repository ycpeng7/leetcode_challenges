class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def _charToIndex(self, ch: str):
        return ord(ch) - ord('a')
    
    def insert(self, key: str):
        trav = self.root
        for ch in key:
            index = self._charToIndex(ch)
            if not trav.children[index]:
                trav.children[index] = TrieNode()
            trav = trav.children[index]
        trav.isEndofWord = True

    def search(self, key: str):
        trav = self.root
        for ch in key:
            index = self._charToIndex(ch)
            if not trav.children[index]:
                return False
            trav = trav.children[index]
        return trav.isEndofWord

if __name__ == "__main__":
    trie = Trie()
    trie.insert('abcd')
    trie.insert('abc')
    trie.insert('bcd')
    print(trie.search('ab'))
    print(trie.search('abc'))
    print(trie.search('abcd'))
    print(trie.search('abcde'))

