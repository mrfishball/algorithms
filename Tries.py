# Use case: Find if any or how many contacts that has a prefix or starts with certain patterns.
# Very much like a dictionary look up.

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_word = False
        self.words_count = 0

    def get_child(self, c):
        for child in self.children:
            if child.char == c:
                return child
        return None

class Trie(object):
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        curr = self.root
        for c in word:
            next_node = curr.get_child(c)
            if next_node is None:
                next_node = TrieNode(c)
                curr.children.append(next_node)
            next_node.words_count += 1
            curr = next_node
        curr.is_word = True

    def find(self, partial):
        curr = self.root
        for c in partial:
            next_node = curr.get_child(c)
            if next_node is None:
                return 0
            curr = next_node
        return curr.words_count
