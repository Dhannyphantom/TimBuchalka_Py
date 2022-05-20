print("Input a decimal to be converted to binary")
number = int(input())

result = number // 2
resultOctal = number // 8
binList = [number % 2]
octalList = [number % 8]

while result != 0:
    binList.append(result % 2)
    result //= 2

while resultOctal != 0:
    octalList.append(result % 8)
    resultOctal //= 8

print("In Binary: ")
for num in reversed(binList):
    print(num, end="")

print(octalList)

print("In Octal: ")
for num in reversed(octalList):
    print(num, end="")
