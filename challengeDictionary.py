locations = {
    0: "You quit the game",
    1: "You are walking on the ROAD, where to next?",
    2: "You are at the top of a HILL, climb down?",
    3: "You are in a BUILDING, wanna rest?",
    4: "You are alone in the VALLEY, wanna run?",
    5: "You somehow end up in the FOREST, wanna hunt?"
}

exits = {
    0: "",
    1: {"N": 5, "W": 2, "E": 3, "S": 4},
    2: {"N": 5},
    3: {"W": 1},
    4: {"N": 1, "W": 2},
    5: {"W": 2, "S": 1}
}

vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W"
}

currLocation = 1
while True:
    print(locations[currLocation])
    avail_exits = ", ".join(exits[currLocation].keys())
    print("Available exists are {}".format(avail_exits))
    inputLoc = input().upper()
    if inputLoc == "Q":
        print(locations[0])
        break
    elif len(inputLoc) > 1:
        words = inputLoc.split()
        for word in words:
            if word in vocabulary:
                inputLoc = vocabulary[word]
                currLocation = exits[currLocation][inputLoc]
    elif inputLoc not in exits[currLocation]:
        print("Invalid response, choose a valid exit")
        inputLoc = input().upper()
    else:
        currLocation = exits[currLocation][inputLoc]
