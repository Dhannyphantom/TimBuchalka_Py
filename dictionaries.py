human = {
    "name": "Daniel",
    "age": 23,
    "height": 29,
    "color": "blue"
}

# print(human["height"])
# del human["age"]
# human.clear()
# while True:
#     dict_key = input("Enter a key: ")
#     if dict_key == "quit":
#         break
#     if dict_key in human:
#         keyValue = human.get(dict_key)
#         print(keyValue)
#     else:
#         print("Invalid key")

for prop in human:
    print(prop + ": " + str(human[prop]))
