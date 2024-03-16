def isValid(s: str) -> bool:
    brackets = {'[': ']', '{': '}', '(': ')'}
    stack = []
    if len(s) % 2 != 0:
        return False
    for bracket in s:
        if bracket in brackets:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != brackets[stack.pop()]:
            return False
    return len(stack) == 0


user_input = '(){}'
print(isValid(user_input))


"""Alternative solution"""
#     def isValid(s: str) -> bool:
#         parentheses = {']': '[', '}': '{', ')': '('}
#         open_par = ['dummy']
#         if s[0] in parentheses:
#             return False
#         elif len(s) % 2 != 0:
#             return False
#         for symbol in s:
#             if symbol in parentheses.values():
#                 open_par.append(symbol)
#             elif symbol in parentheses:
#                 if parentheses[symbol] != open_par[-1]:
#                     return False
#                 else:
#                     open_par.pop()
#
#         if len(open_par) == 1:
#             return True
#         else:
#             return False
