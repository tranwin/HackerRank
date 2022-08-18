# For this challenge, we need to know the 2nd lowest score.
# Let's create a list of scores, as well as a Master list of names + score
MasterList = []
ScoreList = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    MasterList += [[name,score]]
    ScoreList += [score]

# Identify the 2nd lowest score, which has an index of '1' in the ScoreList
SecondLowestScore = sorted(list(set(ScoreList)))[1]

# print (SecondLowestScore)

#Print out names of the students with 2nd lowest score from the MasterList
for x , y in sorted(MasterList):
    if y == SecondLowestScore:
        print(x)

