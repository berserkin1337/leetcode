class WordDictionary:
    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.isWord = False
    def addWord(self, word: str) -> None:
        cur  = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        if self._search(cur,word):
            return True      
    def _search(self,child,word):    
        cur = child
        for i,c in  enumerate(word):
            if c == '.':
                if i == len(word) - 1:
                    for child in  cur.children.values():
                        if child.isWord:
                            return True
                    return False
                
                for child in cur.children.values() :
                    if self._search(child,word[i+1:]):
                        return True
                
                return False
            # print(c,word)
            if c not in cur.children:
                return False
            cur  = cur.children[c]
            # print(cur.isWord)
        return cur.isWord
        
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)