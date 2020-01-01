class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = False
        start = 0
        end = 0
        for i, c in enumerate(s):
            if c != " " and not word:
                start = end = i
                word = True
            elif c != " " and word:
                end = i
            elif word:
                stack.append(s[start:end+1])
                word = False
        if word:
            stack.append(s[start:end+1])
        result = ""
        while stack:
            result += stack.pop() + " "
        return result[0:-1] 