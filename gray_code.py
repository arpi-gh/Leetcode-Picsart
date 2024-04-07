# def grayCode(n: int) -> list[int]:
#     result = []
#     for i in range(2 ** n):
#         binary = bin(i)
#         res = binary[:3]
#         for d in range(3, len(binary)):
#             res += str(int(binary[d - 1]) ^ int(binary[d]))
#         result.append(int(res, 2))
#     return result

def grayCode(n: int) -> list[int]:
    result = []
    for i in range(2 ** n):
        result.append(i ^ i >> 1)
    return result
