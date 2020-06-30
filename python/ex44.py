def recursive_binary_search(list, item, high, low):
    if(low > high):
        return None

    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
        return mid
    if guess > item:
        return recursive_binary_search(list, item, mid - 1, low)
    else:
        return recursive_binary_search(list, item, high, mid + 1)

my_list = [1, 3, 5, 7, 9, 90]

print(recursive_binary_search(my_list, 9, len(my_list), 0))
print(recursive_binary_search(my_list, -1, len(my_list), 0))