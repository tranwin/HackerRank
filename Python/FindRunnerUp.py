n = int(input())
arr = map(int, input().strip().split())

unique_list = []

for i in arr:
    if i not in unique_list:
        unique_list.append(i)
    

unique_list.sort()

index_of_second = len(unique_list)-2

print(unique_list[index_of_second])

