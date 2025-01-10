class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = max(len(word1), len(word2))
        res = ''
        for i in range(length):
            if i < len(word1) and i < len(word2):
                res += word1[i] + word2[i]
            elif i < len(word1):
                res += word1[i]
            else:
                res += word2[i]
        return res
