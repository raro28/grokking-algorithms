def multiplyTable(array):
    result = []
    for i in range(len(array)):
        result.append([array[j]*array[i] for j in range(len(array))])
    return result

print(multiplyTable([1,2,3,4,5]))