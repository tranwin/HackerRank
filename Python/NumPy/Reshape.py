import numpy

def reshape(arr):
    a = numpy.array(arr, int)
    b = numpy.reshape(a,(3,3))
    return b

arr = input().strip().split(' ')
result = reshape(arr)
print(result)