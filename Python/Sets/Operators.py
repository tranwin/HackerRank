n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    x = input().split()
    if len(x) == 1:
        s.pop()
    elif len(x) == 2 and x[0] == 'remove':
        s.remove(int(x[1]))
    elif len(x) == 2 and x[0] == 'discard':
        s.discard(int(x[1]))
        
print(sum(s))
    