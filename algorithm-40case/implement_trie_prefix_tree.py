# @program: PyDemo
# @description: https://leetcode.com/problems/implement-trie-prefix-tree/
# @author: wqdong
# @create: 2019-08-26 09:43

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

s = Trie()
s.insert("apple")

if s.search("apple"):
    print("is word! in trie!")
if s.startsWith("app"):
    print("not word! in trie!")
if not s.search("bank"):
    print("not in trie!")

