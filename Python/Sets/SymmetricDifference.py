# m = int(input())
# a = set(map(int, input().split()))

# n = int(input())
# b = set(map(int, input().split()))

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

c = a - b
d = b - a
e = c.union(d)

print (*sorted(e), sep = '\n')
