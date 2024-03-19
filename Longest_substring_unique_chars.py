def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    end = 0
    max_substring = 0
    substring = 0
    symbols = 95 * [0]
    while start <= end < len(s):
        index = ord(s[end]) - 32
        if symbols[index] == 0:
            symbols[index] = 1
            substring += 1
            end += 1
        else:
            start += 1
            symbols = 95 * [0]
            end = start
            substring = 0
        if substring > max_substring:
            max_substring = substring
    return max_substring


s1 = "abcabbabcd"
print(lengthOfLongestSubstring(s1))