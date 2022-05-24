my_list = ["a", "b", "c", "d"]
myAlphas = "abcdefghijklmnopqrstuvwxyz"

myString = ""
# Strings are immutable and therefore each time
# in the loop a new string is created which is like
# memory tasking and stuff

# for item in my_list:
#     myString += item + ', '

# TO fix that we use the join method for a simple string manipulation

print(", ".join(my_list))
print(", ".join(myAlphas))


