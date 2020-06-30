def iterative_sum(arr):
    result = 0
    for n in arr:
        result +=n
    
    return result

def recursive_sum(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    return arr.pop(0) + recursive_sum(arr)

print(iterative_sum([2,4,6]))
print(recursive_sum([2,4,6]))