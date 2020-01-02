class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pointer = 0
        last_seen = None 
        for i in range(len(typed)):
            if pointer < len(name) and name[pointer] == typed[i]:
                pointer += 1
                last_seen = typed[i]
            elif typed[i] == last_seen:
                continue 
            else:
                return False
        if pointer != len(name):
            return False
        return True 