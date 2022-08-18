n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
query_name = input()

# List score list accordsing to the query_name
query_name_scores = student_marks[query_name]

# Find average
def find_average(List):
    return sum(List) / len(List)

# print(scores)
# print(query_name_scores)

# Print the average scores with 2 decimal places
print("{:.2f}".format(find_average(query_name_scores)))

