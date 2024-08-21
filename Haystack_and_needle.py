class Solution(object):
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        hay = len(haystack)
        need = len(needle)
        for i in range(hay-need+1):
            current = i
            found = True
            for letter in range(need):
                if haystack[current] == needle[letter]:
                    current += 1
                else:
                    found = False
            if found:
                return i
        return -1



sol = Solution()
print(sol.strStr('sabutsad', 'sad'))