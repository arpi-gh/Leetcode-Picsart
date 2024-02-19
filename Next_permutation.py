'''The rules are:
if last two elems sorted-> reverse order
if reverse:
if preceding elem smaller than the greatest on the right side, swap it with its next num. on the right, sort the right side
'''

def next_permutation(array):
    if array == sorted(array, reverse=True):
        array.sort()
        return
    order = list(set(sorted(array)))
    i = len(array) - 1   # start from the last element
    while i > 0:
        if array[i] <= array[i-1]:  # If the order is reversed
            if array[i-2] < max(array[i-1:]):  # if the previous element is less than the max of the right side
                target = order.index(array[i-2]) + 1
                for num in sorted(array[i-2:]):  # look for its next upgrade in the order
                    if num in order[target:]:  # if found the upgrade
                        upgrade_index = i - 2 + array[i-2:].index(num)  # remember its index in the array
                        array[i-2], array[upgrade_index] = array[upgrade_index], array[i-2]  # swap the places
                        array[i-1:] = sorted(array[i-1:])  # Sort the rest
                        i = -1  # stop the iteration
                        break
            i -= 1  # otherwise start over
        elif array[i] == array[i-1]:
            i -= 1
        else:  # If the order of the elements is sorted
            array[i], array[i-1] = array[i-1], array[i]  # Reverse the order of just the last two elements
            i = -1  # stop the iteration
    return


if __name__ == '__main__':
    test_cases = [[2, 2, 7, 5, 4, 3, 2, 2, 1], [5, 4, 7, 5, 3, 2], [1, 2], [1, 2, 3], [3, 2, 1], [1, 0, 3, 2]]
    for case in test_cases:
        next_permutation(case)
        print(case)



