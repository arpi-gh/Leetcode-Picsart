def romanToInt(s: str) -> int:
    next_num = 0
    result = 0
    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(s) - 1):
        if numerals[s[i]] < numerals[s[i+1]]:
            result -= numerals[s[i]]
        else:
            result += numerals[s[i]]
        next_num = i + 1
    result += numerals[s[next_num]]
    return result


num = 'D'
print(romanToInt(num))
