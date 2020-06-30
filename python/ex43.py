def max(array):
    if(len(array) == 0):
        return None
    if(len(array) == 1):
        return array[0]

    last = array.pop()
    _max = max(array)

    return last if last > _max else _max

print(max([1,2,3,4,5,6,7,8,9]))
print(max([9,8,7,6,5,5,4,3,2,1]))
print(max([-1,67,4,8,4,7,5,7,45,2]))
print(max([1]))
print(max([1,2]))
print(max([3,1]))
print(max([]))