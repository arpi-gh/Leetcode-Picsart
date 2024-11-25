class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 4:
            return False
        num = bin(n)
        trail = len(num) - 3
        if num[2] == '1' and trail % 2 == 0 and int(num[3:]) == 0:
            return True
        return False


if __name__ == '__main__':
    print(Solution().isPowerOfFour(1))