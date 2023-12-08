def list_to_entry(lst: list) -> str:
    to_add = ''
    x = 0
    for i in lst:
        if type(i) == int:
            to_add += str(i)
            continue
        to_add += f"'{i}'"
        if len(lst) - 1 != x:
            to_add += ","
        x += 1
    return to_add

'''
Building Trie Entities
- Used for searching and creating users
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c in cur.children:
                print(cur.children)
                cur = cur.children[c]
            else:
                return "Item not in list"
        return "Item in list"

    def starts_with(self, word):
        cur = self.root
        for c in word:
            if c in cur.children and not cur.children[c].endOfWord:
                print(cur.children)
                cur = cur.children[c]
            else:
                return "Item not in list"
        return "Item in list"
