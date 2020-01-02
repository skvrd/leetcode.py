from typing import List

class WordDistance:

    def __init__(self, words: List[str]):
        self.words = {}
        for index, word in enumerate(words):
            positions = self.words.get(word, [])
            positions.append(index)
            self.words[word] = positions

    def shortest(self, word1: str, word2: str) -> int:
        word1_pos = self.words[word1]
        word2_pos = self.words[word2]
        distance = abs(word1_pos[0] - word2_pos[0])
        for pos1 in word1_pos:
            for pos2 in word2_pos:
                distance = min(distance, abs(pos1 - pos2))
        return distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)