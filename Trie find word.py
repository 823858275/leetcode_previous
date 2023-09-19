from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word.split(" "):
            cur = cur.children[w]
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word.split(" "):
            if w not in cur.children:
                return False
            cur = cur.children[w]
        if cur.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for p in prefix.split(" "):
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True


def find_location_from_doc(location_list, doc):
    res = []
    location_trie = Trie()
    for location in location_list:
        location_trie.insert(location)
    doc_list = doc.split(" ")
    i = 0
    while i < len(doc_list):
        if location_trie.startsWith(doc_list[i]):
            j = 1
            while i + j + 1 <= len(doc_list) and location_trie.search(" ".join(doc_list[i:i + j + 1])):
                j += 1
            res.append(" ".join(doc_list[i:i + j]))
            i = i + j
        i += 1
    return res


location_list = ["new york", "new york city", "ab", "ac acd ef", "ae", "ac acd", "ab ac"]
doc = "i like new york ac ae ar ab ac"

res = find_location_from_doc(location_list, doc)
print(res)
