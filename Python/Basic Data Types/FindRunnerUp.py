n = int(input())
arr = map(int, input().strip().split())

# Create  a list with n items and sort ascending
UniqueList = []

for i in arr:
    if i not in UniqueList:
        UniqueList.append(i)
    

UniqueList.sort()

# Index the runner-up

RunnerUp_index = len(UniqueList)-2

print(UniqueList[RunnerUp_index])

