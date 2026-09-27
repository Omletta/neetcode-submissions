class PrefixTree:

    def __init__(self):
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node[self.end] = True


    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]

        return self.end in node
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
        
        