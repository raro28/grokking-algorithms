def recursiveCount(array):
    if(len(array) == 0):
        return 0
    if(len(array) == 1):
        return 1

    array.pop()
    return 1 + recursiveCount(array)

array = [1,2,4,5,6,7,8,9]
print(recursiveCount(array))