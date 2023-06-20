def findMissingNumbers(n):
    numbers = set(n)
    x = sorted(numbers)
    length = len(n)
    output = []
    for i in range(0, x[-1]):
        if i not in x:
            output.append(i)
    return output

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 19, 20]

print(findMissingNumbers(listOfNumbers))