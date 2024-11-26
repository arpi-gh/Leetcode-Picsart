class Solution:
     # regular solution
    # def makeGood(self, s: str) -> str:
    #     last = len(s) - 1
    #     i = 0
    #     while i < last:
    #         if abs(ord(s[i]) - ord(s[i + 1])) == 32:
    #             s = s[:i] + s[i + 2:]
    #             last -= 2
    #             if i > 0:
    #                 i -= 1
    #         else:
    #             i += 1
    #
    #     return s

     # stack solution
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
            else:
                 stack.append(s[i])
            i += 1
        return "".join(stack)




if __name__ == '__main__':
    print(Solution().makeGood('abBAcC'))

