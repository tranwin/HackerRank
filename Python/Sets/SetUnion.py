# number of students who have subscribed to the English newspaper
n = int(input())
m = set(map(int, input().split()))

# number of students who have subscribed to the French newspaper
b = int(input())
c = set(map(int, input().split()))

print (len(m.union(c)))