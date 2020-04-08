from collections import defaultdict

DefaultDict=defaultdict(list)
people = [['male','winter'],['female','elly'], ['male','frank'], ['female','emma']]
for info in people:
    DefaultDict[info[0]].append(info[1])
print(DefaultDict)