
def intToRoman(num: int) -> str:
    result = ''
    numerals = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    if num in numerals:
        return numerals[num]
    div = 1000
    while num > 0:
        res = num // div
        if res >= 1:
            if res == 9:
                result = result + numerals[div] + numerals[div*10]
            elif res == 4:
                result = result + numerals[div] + numerals[5*div]
            elif res >= 5:
                result = result + numerals[5 * div] + (res-5) * numerals[div]
            elif res < 4:
                result = result + (res * numerals[div])
        num = num - res * div
        div //= 10
    return result


n = 40
print(intToRoman(n))
