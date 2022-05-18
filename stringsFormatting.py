age = 24

print("My age is " + str(age) + " years")

# STRING REPLACEMENT

print("My age is {0} years".format(age))
print("My name is {0} and I'm {1} years old, I like {2} and dislike {3}"
      .format("Daniel", 24, "Football", "Programming"))

# the numbers or indexing can be re-used

# print("""
#     January: {2},
#     February: {0},
#     March: {2},
#     April: {1},
#     May: {2},
#     June: {1},
# """.format(29, 30, 31))


# PYTHON 2 FORMATS
print("My age is %d years" % age)
print("My name is %s and I'm %d years old and I love %s" % ("Daniel", 24, "Programming"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print()

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# we can left justify or right justify by adding < or >
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
