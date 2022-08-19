import numpy

r, c =list(map(lambda x:int(x),input().split()))
lst = []

# Create a list of input integers:
for i in range(r):
    lst.append(list(map(lambda x:int(x),input().split())))

my_array = numpy.array(lst)

print(numpy.transpose(my_array))
print(my_array.flatten())
