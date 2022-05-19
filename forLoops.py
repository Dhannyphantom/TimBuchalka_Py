# for i in range(1, 21):
#     print("i is now {}".format(i))

numbers = "9,644,654,732,356,232,643"
# for i in range(0, len(numbers)):
#     if numbers[i] in "0123456789":
#         print(numbers[i])

for char in numbers:
    if char in "0123456789":
        print(char)
