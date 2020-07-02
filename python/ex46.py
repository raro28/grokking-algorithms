def double(array):
    for i in range(len(array)):
        array[i] *= 2
    
    return array

print(double([1,2,3,4,5,6]))