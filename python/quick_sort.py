import random

def pick_pivot(array):
    return random.randint(0, len(array) - 1)

def getpartitions(pivot, array):
    result = [[], []]
    for i in range(len(array)):
        item = array[i]
        if(i != pivot):
            if(item <= array[pivot]):
                result[0].append(item)
            else:
                result[1].append(item)
    return result


def quick_sort(array):
    if len(array) < 2:
        return array.copy()
    else:
        result = []
        pivot = pick_pivot(array)
        partitions = getpartitions(pivot, array)
        return quick_sort(partitions[0]) + [array[pivot]] + quick_sort(partitions[1])


print("\nresults\n")
print(quick_sort([1, 2, 3, 4, 5]))
print(quick_sort([5, 4, 3, 2, 1]))
print(quick_sort([5, 4, 6, 2, 1]))
