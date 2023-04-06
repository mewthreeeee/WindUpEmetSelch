import pyperclip

spread = { #Must add to 1
    "idle": 0.8,
    "moveRandomly": 0.2
}
sortedSpread = sorted(spread.items(), key=lambda x:x[1])

actionsList = [""]
probabilityList = [0]
accumulator = 0
for i in sortedSpread:
    accumulator += i[1]
    actionsList.append(i[0])
    probabilityList.append(accumulator)

jsonStringActions = "\"actions\": ["
jsonStringProbabilities = "\"probabilities\": ["

for i in range(len(sortedSpread)+1):
    jsonStringActions += f"\"{actionsList[i]}\", "
    jsonStringProbabilities += f"{probabilityList[i]}, "

jsonStringActions = jsonStringActions[:-2] + "],"
jsonStringProbabilities = jsonStringProbabilities[:-2] + "],"

print("String added to clipboard:")
print(jsonStringActions)
print(jsonStringProbabilities)
pyperclip.copy(f"{jsonStringActions}\n{jsonStringProbabilities}")