import numpy

r, c =input().split()
r = int(r)
lst = []

# Create a list consisting of input values
for i in range(r):
    lst.append(input().split())

my_array = numpy.array(lst)

print(numpy.transpose(my_array))
print(my_array.flatten())