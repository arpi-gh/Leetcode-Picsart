# 1 2 3 4 5  if sorted, reverse the order of the last two elems
# 1 2 3 5 4  if order of subarray is reversed, increase the preceding number to the next lowest number
# 1 2 4 3 5  if sorted, reverse the order of the last two elems
# 1 2 4 5 3  if order is reversed, increase the preceding number to the next lowest number, sort the rest
# 1 2 5 3 4  if sorted, reverse the order of the last two elems
# 1 2 5 4 3  if reversed, increase the preceding num to the next lowest number
# 1 3 2 4 5  if sorted, reverse the order of preceding two elems
# 1 3 4 2 5  if not sorted but not reversed either, go to next subarray, reverse the order
# 1 3 4 5 2
# 1 3 5 2 4
# 1 3 5 4 2
# 1 4 2 3 5
# 1 4 3 2 5
# 1 4 3 5 2
# 1 4 5 2 3
# 1 4 5 3 2

'''The rules are:
if the last 2 elems of subarray are sorted, reverse the order
then increase the preceding elem to the next lowest elem if there is one, if not
go the preceding elem, increase that one, sort the rest(starting from the lowest number)
start from the last two elems again

need to update the numbers list with each iteration
'''


def next_perm(array):
    numbers = list(set(sorted(array)))
    i = len(array) - 1  # the index of the last element
    j = 1  # an index to help us shift to the left
    if array[i] > array[i - j]:  # if the last two elements are sorted
        array[i], array[i - j] = array[i - j], array[i]  # reverse the order
    elif array[i] < array[i - j]:  # if the order is reverse
        j += 1  # prepare to shift to the left
        while j <= i:  # while there's room to shift
            if array[i - j] != numbers[-1]:  # if the preceding element is not the largest number
                tmp = array[i - j]  # store its value
                next_number_index = numbers.index(tmp) + 1
                array[i - 2] = numbers[next_number_index]  # increase it to the next lowest
                break
            j += 1  # otherwise shift to the left again
