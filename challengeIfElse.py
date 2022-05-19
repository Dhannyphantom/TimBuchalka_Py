print("What is your name?")
name = input()
print("How old are you?")
age = int(input())

if 18 <= age <= 30:
    print("Welcome {}!, to the Holiday".format(name))
else:
    print("Sorry {}, you're not eligible".format(name))
