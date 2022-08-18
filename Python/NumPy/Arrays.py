import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a = numpy.array(arr, float)
    b = a[::-1]
    return b
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)