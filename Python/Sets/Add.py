n = int(input())
s = []
for i in range(n):
    a = input()
    s.append(a)

print(len(set(s)))


# shorter 
# s = set(input() for _ in range(n))