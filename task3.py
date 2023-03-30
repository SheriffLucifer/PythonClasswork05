def findNumber(tmpList):
    count = 0
    for i in range(1, len(tmpList) - 1):
        if tmpList[i - 1] < tmpList[i] > tmpList[i + 1]:
            count += 1
        return count

list = [1, 2, 3, 4, 5]

print(findNumber(list))