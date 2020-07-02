import random


def pick_pivot(array):
    return random.randint(0, len(array) - 1)


def quick_sort(array):
    if len(array) < 2:
        return array.copy()
    else:
        result = []
        pivot = pick_pivot(array)
        #https://realpython.com/list-comprehension-python/
        less = [array[i] for i in range(
            len(array)) if i != pivot and array[i] <= array[pivot]]
        greater = [array[i] for i in range(
            len(array)) if i != pivot and array[i] > array[pivot]]

        return quick_sort(less) + [array[pivot]] + quick_sort(greater)


print("\nresults\n")
print(quick_sort([1, 2, 3, 4, 5]))
print(quick_sort([5, 4, 3, 2, 1]))
print(quick_sort([5, 4, 6, 2, 1]))
