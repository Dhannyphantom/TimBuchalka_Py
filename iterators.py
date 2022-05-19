numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

numbers_iter = iter(numbers)

for i in range(0, len(numbers)):
    print(next(numbers_iter))
