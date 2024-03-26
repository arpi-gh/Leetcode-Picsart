def hammingWeight(n: int) -> int:
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count


print(hammingWeight(25))