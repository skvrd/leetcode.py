from typing import List

class Trie:
    word_end = False
    
    def __init__(self):
        self.children = dict()
    
    def insert(self, word:str) -> None:
        if not len(word):
            self.word_end = True
            return
        node = self.children.get(word[0], Trie())
        self.children[word[0]] = node
        node.insert(word[1:])
        
    def _find_prefix_node(self, prefix:str):
        if not len(prefix):
            return self
        node = self.children.get(prefix[0], None)
        if node:
            return self.children[prefix[0]]._find_prefix_node(prefix[1:])
        return node
            
        
    def suggest(self, prefix:str, number:int=3):
        def helper(prefix:str, node:Trie, number:int, result:List[str]):
            if not node:
                return
            if len(result) >= number:
                return
            if not len(node.children):
                result.append(prefix)
                return
            if node.word_end:
                result.append(prefix)
            for char in sorted(node.children):
                helper(f"{prefix}{char}", node.children[char], number, result)
            
        result = []
        node = self._find_prefix_node(prefix)
        helper(prefix, node, number, result)
        return result
                
        

class Solution:
    
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        result = []
        for i in range(len(searchWord)):
            result.append(trie.suggest(searchWord[:i+1], 3))
        return result